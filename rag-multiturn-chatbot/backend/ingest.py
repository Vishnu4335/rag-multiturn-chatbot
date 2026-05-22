import os

from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS

from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

DATA_PATH = "data"


def load_documents():

    documents = []

    for file in os.listdir(DATA_PATH):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(DATA_PATH, file)

            loader = PyPDFLoader(pdf_path)

            docs = loader.load()

            for doc in docs:
                doc.metadata["source"] = file

            documents.extend(docs)

    return documents


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    return splitter.split_documents(documents)


def create_vectorstore(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    vectorstore.save_local("vectorstore")


if __name__ == "__main__":

    print("Loading PDFs...")

    docs = load_documents()

    print(f"Loaded {len(docs)} pages")

    print("Splitting documents...")

    chunks = split_documents(docs)

    print(f"Created {len(chunks)} chunks")

    print("Creating vector DB...")

    create_vectorstore(chunks)

    print("Vector DB created successfully")