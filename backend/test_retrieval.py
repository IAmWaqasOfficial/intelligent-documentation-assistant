from app.services.embedding_service import generate_embeddings
from app.services.vector_store import create_vector_index
from app.services.retriever import retrieve_relevant_chunks


chunks = [
    "FastAPI is a modern web framework for building APIs with Python.",
    "Python is a popular programming language used for software development.",
    "FAISS is a library for efficient similarity search.",
]


# 1. Generate embeddings for document chunks
document_embeddings = generate_embeddings(chunks)


# 2. Create FAISS index
index = create_vector_index(document_embeddings)


# 3. User asks a question
question = "what is FIASS?"


# 4. Generate embedding for the question
query_embedding = generate_embeddings([question])[0]


# 5. Retrieve relevant chunks
relevant_chunks = retrieve_relevant_chunks(
    index,
    chunks,
    query_embedding,
    top_k=2
)


print("Relevant chunks:")

for chunk in relevant_chunks:
    print("\n---")
    print(chunk)