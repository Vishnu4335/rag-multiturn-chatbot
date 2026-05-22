import os

from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from transformers import pipeline

load_dotenv()

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector DB
vectorstore = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

# Local HuggingFace model
generator = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)


def ask_question(question):

    # Search similar docs
    docs = vectorstore.similarity_search(question, k=3)

    # Combine context
    context = "\n\n".join([
        doc.page_content for doc in docs
    ])

    prompt = f"""
Answer ONLY from the provided context.

If answer is not found, say:
"I could not find this information in the company documents."

Context:
{context}

Question:
{question}

Answer:
"""

    # Generate answer
    result = generator(
        prompt,
        max_new_tokens=200
    )

    answer = result[0]["generated_text"]

    citations = []

    for doc in docs:
        source = doc.metadata.get("source", "Unknown")

        if source not in citations:
            citations.append(source)

    return {
        "answer": answer,
        "citations": citations
    }