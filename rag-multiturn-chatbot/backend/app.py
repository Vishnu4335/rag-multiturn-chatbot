from fastapi import FastAPI
from pydantic import BaseModel
import traceback

from rag_pipeline import ask_question

app = FastAPI()


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "RAG API Running"}


@app.post("/chat")
def chat(request: ChatRequest):

    try:

        result = ask_question(request.question)

        return {
            "question": request.question,
            "answer": result["answer"],
            "citations": result["citations"]
        }

    except Exception as e:

        print(traceback.format_exc())

        return {
            "error": str(e)
        }