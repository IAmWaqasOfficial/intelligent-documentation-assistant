from app.services.embedding_service import generate_embeddings


chunks = [
    "FastAPI is a modern web framework for building APIs with Python.",
    "Python is a popular programming language."
]


embeddings = generate_embeddings(chunks)


print("Number of embeddings:", len(embeddings))
print("Embedding dimensions:", len(embeddings[0]))
print("First embedding:")
print(embeddings[0])