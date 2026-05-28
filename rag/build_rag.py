from rag.loader import load_docs
from rag.chunker import chunk_docs
from rag.vector_store import create_vectorstore

from tools.rag_tool import build_rag_chain


def initialize_rag():

    docs = load_docs(
        "data/reliance.pdf"
    )

    chunks = chunk_docs(docs)

    vectorstore = create_vectorstore(
        chunks
    )

    rag = build_rag_chain(
        vectorstore
    )

    return rag