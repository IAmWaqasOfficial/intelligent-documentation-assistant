from fastapi import APIRouter, UploadFile, File, HTTPException


from app.config import UPLOAD_FOLDER
from app.services.document_processor import extract_and_chunk_pdf
from app.services.embedding_service import generate_embeddings
from app.services.vector_store import create_vector_index
from app.services.document_store import documents

router = APIRouter()


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    # Validate file type
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    file_path = f"{UPLOAD_FOLDER}/{file.filename}"

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    result = extract_and_chunk_pdf(file_path)

    document_text = result["text"]

    chunks = result["chunks"]

    # Generate embeddings
    embeddings = generate_embeddings(chunks)

    # Create FAISS vector index
    index = create_vector_index(embeddings)

    # Store processed document
    documents[file.filename] = {
    "text": document_text,
    "chunks": chunks,
    "index": index
}

    return {
        "filename": file.filename,
        "chunks": len(chunks),
        "message": "Document uploaded and processed successfully."
    }