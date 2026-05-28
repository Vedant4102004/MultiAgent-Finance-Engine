def build_rag_chain(vector_store):

    def retrieve(query: str):

        docs = vector_store.similarity_search(
            query,
            k=3
        )

        context = "\n".join(
            [doc.page_content for doc in docs]
        )

        return context

    return retrieve


def retrieve_docs(query: str):
    pass