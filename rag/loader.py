from langchain_community.document_loaders import PyPDFLoader, TextLoader

def load_docs(file_path: str):
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path)

    docs = loader.load()
    return docs
    
