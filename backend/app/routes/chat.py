from fastapi import APIRouter, HTTPException

from app.models.schemas import QuestionRequest
from app.services.document_store import documents
from app.services.embedding_service import generate_embeddings
from app.services.retriever import retrieve_relevant_chunks
from app.services.gemini_service import generate_answer

router = APIRouter()


@router.post("/ask")
async def ask_question(request: QuestionRequest):
    # Check if document exists
    if request.filename not in documents:
        raise HTTPException(
            status_code=404,
            detail="Document not found."
        )

    # Get uploaded document
    document = documents[request.filename]

    # Generate embedding for the user's question
    query_embedding = generate_embeddings([request.question])

    # Retrieve relevant chunks
    relevant_chunks = retrieve_relevant_chunks(
        index=document["index"],
        chunks=document["chunks"],
        query_embedding=query_embedding
    )

    # Combine retrieved chunks into context
    context = "\n\n".join(relevant_chunks)

    # Generate AI answer
    answer = generate_answer(
        question=request.question,
        context=context
    )

    return {
        "question": request.question,
        "answer": answer,
        "relevant_chunks": relevant_chunks
    }