from fastapi import FastAPI, UploadFile, File

from app.services.document_processor import extract_and_chunk_pdf
from app.services.embedding_service import generate_embeddings
from app.services.vector_store import create_vector_index
from app.services.document_store import documents

from app.services.gemini_service import generate_answer

from app.services.document_store import documents
from app.services.retriever import retrieve_relevant_chunks

from app.services.embedding_service import generate_embeddings


from app.models.schemas import QuestionRequest


app = FastAPI(
    title="Intelligent Documentation Assistant",
    description="An AI-powered platform for understanding and interacting with technical documentation.",
    version="1.0.0"
)



@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    if file.content_type != "application/pdf":
        return {
            "error": "Only PDF files are allowed"
        }

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    # 1. Extract text and split into chunks
    chunks = extract_and_chunk_pdf(file_path)

    # 2. Generate embeddings
    embeddings = generate_embeddings(chunks)

    # 3. Create FAISS index
    index = create_vector_index(embeddings)

    # 4. Store the processed document
    documents[file.filename] = {
        "chunks": chunks,
        "index": index
    }

    return {
        "filename": file.filename,
        "chunks": len(chunks),
        "message": "Document uploaded and processed successfully"
    }


@app.post("/ask")
async def ask_question(request: QuestionRequest):

    # Check if the document exists
    if request.filename not in documents:
        return {
            "error": "Document not found."
        }

    # Get the uploaded document
    document = documents[request.filename]

    # Generate question embedding
    query_embedding = generate_embeddings(
        [request.question]
    )

    # Retrieve relevant chunks
    relevant_chunks = retrieve_relevant_chunks(
        index=document["index"],
        chunks=document["chunks"],
        query_embedding=query_embedding
    )

    # Combine retrieved chunks into a single context
    context = "\n\n".join(relevant_chunks)

    # Generate AI answer
    answer = generate_answer(
        question=request.question,
        context=context
    )

    # Create response
    response = {
        "question": request.question,
        "answer": answer,
        "relevant_chunks": relevant_chunks
    }

    print(response)

    return response