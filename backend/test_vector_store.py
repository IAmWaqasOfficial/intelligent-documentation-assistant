from app.services.embedding_service import generate_embeddings
from app.services.vector_store import (
    create_vector_index,
    search_vector_index
)


chunks = [
    "FastAPI is a modern web framework for building APIs with Python.",
    "Python is a popular programming language.",
    "FAISS is used for similarity search."
]


document_embeddings = generate_embeddings(chunks)

index = create_vector_index(document_embeddings)


question = "How can I build an API with Python?"

question_embedding = generate_embeddings([question])[0]


distances, indices = search_vector_index(
    index,
    question_embedding,
    top_k=2
)


print("Distances:", distances)
print("Indices:", indices)


for index_number in indices[0]:

    print("Matching chunk:")
    print(chunks[index_number])