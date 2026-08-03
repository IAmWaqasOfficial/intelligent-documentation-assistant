# 📄 Intelligent Documentation Assistant

> An AI-powered RAG (Retrieval-Augmented Generation) system that lets you upload technical documentation and have intelligent, context-aware conversations with it.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-1.45+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Gemini_AI-Google-4285F4?style=for-the-badge&logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-In_Development-FFA500?style=for-the-badge" />
</p>

---

## 🧠 What It Does

Technical documentation can be hundreds of pages long. The **Intelligent Documentation Assistant** solves this by:

1. **Accepting your PDF documents** via a clean Streamlit interface
2. **Processing them through a RAG pipeline** — chunking, embedding, and indexing content
3. **Answering your questions** with context pulled directly from your uploaded document — not from general AI knowledge

No more ctrl+F. Just ask.

---

## 🏗️ Architecture

```
User uploads PDF
      │
      ▼
FastAPI Backend (/upload)
      │
      ├── Extract text from PDF
      ├── Split into semantic chunks
      ├── Generate embeddings (Gemini)
      └── Build FAISS vector index
                    │
                    ▼
         User asks a question
                    │
                    ▼
FastAPI Backend (/ask)
      │
      ├── Embed the question
      ├── Retrieve top-K relevant chunks (FAISS)
      ├── Build context prompt
      └── Generate grounded answer (Gemini LLM)
                    │
                    ▼
         Answer displayed in Streamlit
```

---

## 🗂️ Project Structure

```
intelligent-documentation-assistant/
│
├── backend/                        # FastAPI REST API
│   ├── app/
│   │   ├── main.py                 # API endpoints (/upload, /ask)
│   │   ├── models/
│   │   │   └── schemas.py          # Pydantic request/response models
│   │   └── services/
│   │       ├── document_processor.py   # PDF text extraction & chunking
│   │       ├── embedding_service.py    # Gemini embedding generation
│   │       ├── vector_store.py         # FAISS index creation
│   │       ├── document_store.py       # In-memory document storage
│   │       ├── retriever.py            # Semantic chunk retrieval
│   │       ├── gemini_service.py       # Gemini LLM answer generation
│   │       └── text_splitter.py        # Text splitting utilities
│   ├── uploads/                    # Runtime PDF storage (git-ignored)
│   ├── test_embeddings.py
│   ├── test_retrieval.py
│   ├── test_vector_store.py
│   ├── .env.example                # Environment variable template
│   └── requirements.txt            # Backend Python dependencies
│
├── frontend/                       # Streamlit UI
│   ├── app.py                      # Main Streamlit application
│   └── requirements.txt            # Frontend Python dependencies
│
├── requirements.txt                # Shared/top-level dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend API** | Python, FastAPI, Uvicorn |
| **Frontend UI** | Streamlit |
| **AI / LLM** | Google Gemini API |
| **Embeddings** | Gemini Embedding Model |
| **Vector Search** | FAISS |
| **Document Parsing** | PyMuPDF / PDFPlumber |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Git
- A [Google Gemini API key](https://aistudio.google.com/app/apikey)

### 1. Clone the Repository

```bash
git clone https://github.com/IAmWaqasOfficial/intelligent-documentation-assistant.git
cd intelligent-documentation-assistant
```

### 2. Set Up the Backend

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Configure Environment Variables

```bash
# Inside backend/ folder
cp .env.example .env
```

Open `.env` and add your Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

> ⚠️ **Never commit your `.env` file.** It is already in `.gitignore`.

### 4. Run the Backend

```bash
# From the backend/ directory (with venv active)
uvicorn app.main:app --reload
```

Backend will be live at: **http://127.0.0.1:8000**  
Swagger API docs: **http://127.0.0.1:8000/docs**

### 5. Set Up & Run the Frontend

Open a new terminal:

```bash
cd frontend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

Frontend will open at: **http://localhost:8501**

---

## 📈 Development Status

🚧 **Currently in active development**

### ✅ Completed
- [x] FastAPI backend setup with Uvicorn
- [x] File upload API endpoint (`/upload`)
- [x] PDF text extraction and chunking
- [x] Gemini embedding generation
- [x] FAISS vector index creation
- [x] Semantic retrieval (`/ask` endpoint)
- [x] Gemini LLM answer generation
- [x] Streamlit frontend with chat UI
- [x] Session state & chat history

### 🔄 In Progress
- [ ] Source page references in answers
- [ ] Multiple document support

### 📋 Planned
- [ ] ChromaDB persistent vector store
- [ ] PostgreSQL for document metadata
- [ ] Docker containerization
- [ ] Production deployment

---

## 🔒 Security

- API keys are stored in a `.env` file, which is **git-ignored**
- The `.env.example` file provides a safe template with no real secrets
- Uploaded documents are stored locally and not committed to version control

---

## 🤝 Contributing

This project is currently for educational and portfolio purposes. Feel free to fork and explore.

---

## 👨‍💻 Author

**Waqas Irshad**  
Computer Science Student | Python & FastAPI | AI-Integrated Applications | Flutter

---

## 📄 License

This project is for educational and portfolio purposes.
