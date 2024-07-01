from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os


def load_split_docs(file_name: str) -> list:

    file_path: str = os.path.join("documents", "pdfs", file_name)
    loader = PyPDFLoader(file_path)
    docs: list = loader.load()
    chunk_size: int = 2000
    chunk_overlap: int = 300

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    docs_split: list = splitter.split_documents(docs)

    return docs_split
