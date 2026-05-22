Multi-Turn RAG Chatbot
An end-to-end Retrieval-Augmented Generation (RAG) chatbot built using LangChain, FAISS, FastAPI, Streamlit, and HuggingFace models.

This project enables users to ask questions from company documents using semantic search and AI-generated contextual responses.

Features
Multi-turn conversational chatbot
Retrieval-Augmented Generation (RAG)
PDF document ingestion
Semantic similarity search using FAISS
HuggingFace embeddings
FastAPI backend APIs
Streamlit interactive frontend
Source citation support
Local LLM integration (No paid API required)
Modular and scalable architecture

Tech Stack
Python
LangChain
FAISS
FastAPI
Streamlit
HuggingFace Transformers
Sentence Transformers

Project Workflow
PDF Documents
      ↓
Document Loading
      ↓
Text Chunking
      ↓
Embedding Generation
      ↓
FAISS Vector Store
      ↓
User Query
      ↓
Similarity Search
      ↓
Relevant Context Retrieval
      ↓
LLM Response Generation
      ↓
Final Answer with Citations

Project Structure
rag-multiturn-chatbot/
│
├── backend/
│   ├── data/
│   ├── vectorstore/
│   ├── app.py
│   ├── ingest.py
│   ├── rag_pipeline.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   └── streamlit_app.py
│
└── README.md

Installation
git clone https://github.com/Vishnu4335/rag-multiturn-chatbot.git
cd rag-multiturn-chatbot/backend
pip install -r requirements.txt
python ingest.py
python -m uvicorn app:app --reload

Open new terminal:
cd frontend
streamlit run streamlit_app.py

Key Highlights
Built complete RAG pipeline from scratch
Implemented semantic document retrieval
Designed scalable backend/frontend architecture
Integrated vector database for efficient search
Developed real-world AI document assistant
Demonstrated practical Generative AI application development

Future Improvements
Chat memory support
Multi-document upload
Docker deployment
Cloud deployment
Authentication system
Streaming responses
