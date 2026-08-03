from app.services.vector_store import search_vector_index

def retrieve_relevant_chunks(
    index,
    chunks,
    query_embedding,
    top_k=2
):

    distances, indices = search_vector_index(
        index,
        query_embedding,
        top_k
    )
    relevant_chunks = []

    for index_number in indices[0]:

        relevant_chunks.append(
            chunks[index_number]
        )

    return relevant_chunks