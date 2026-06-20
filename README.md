# 💬 WhatsApp AI Support Agent with RAG

An intelligent WhatsApp customer support agent powered by Groq AI, featuring automatic RAG (Retrieval Augmented Generation) for large knowledge bases and voice message support.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-async-009688)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- 💬 **WhatsApp Integration** — via Twilio API (Meta Cloud API also supported)
- 🧠 **Smart Knowledge Loading** — Automatically switches between simple mode (small docs) and RAG mode (large docs)
- 🔍 **RAG with Vector Search** — Uses sentence-transformers + ChromaDB for accurate retrieval from large documents
- 🎙️ **Voice Message Support** — Transcribes voice messages using Groq Whisper
- 💾 **Conversation Memory** — Redis-backed with automatic in-memory fallback
- 📄 **Multi-format Knowledge Base** — Reads PDF, DOCX, TXT, and websites
- ⚡ **Async Architecture** — Built on FastAPI for production-grade performance
- 📝 **Proper Logging** — All events logged with timestamps

---

## 📁 Project Structure

```
├── app/
│   ├── main.py           → FastAPI entry point
│   ├── webhook.py         → receives WhatsApp messages
│   ├── whatsapp.py         → sends WhatsApp messages (Twilio)
│   ├── ai.py               → Groq AI + RAG integration
│   ├── voice.py             → speech-to-text (Groq Whisper)
│   ├── memory.py            → Redis conversation history
│   ├── knowledge.py          → automatic simple/RAG mode switching
│   ├── extractor.py           → reads PDF/DOCX/TXT/website
│   ├── rag/
│   │   ├── chunker.py          → splits text into chunks
│   │   ├── embedder.py         → text → vectors (sentence-transformers)
│   │   └── vector_store.py     → ChromaDB operations
│   └── logger.py
├── knowledge/              → drop client documents here
├── config.py
├── requirements.txt
```

---

## 🧠 How the Knowledge System Works

```
Knowledge base ≤ 4000 words → SIMPLE MODE
→ Full content sent directly to AI every time

Knowledge base > 4000 words → RAG MODE
→ Document chunked and embedded
→ Only the 3 most relevant chunks retrieved per question
→ Keeps responses fast and accurate regardless of document size
```

This automatic switching means the agent stays efficient whether a client has a 1-page FAQ or a 50-page manual.

---

## ⚙️ Setup & Installation

### 1. Clone and install
```bash
git clone https://github.com/usmanxjavaid/whatsapp-ai-agent
cd whatsapp-ai-agent
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Create `.env`
```env
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
GROQ_API_KEY=your_groq_key
VERIFY_TOKEN=your_secret_token
```

### 3. Add knowledge files
Drop PDF/DOCX/TXT files into `knowledge/` folder.

### 4. Run locally
```bash
uvicorn app.main:app --reload
```

### 5. Expose for webhook testing (local only)
```bash
ngrok http 8000
```
Set the ngrok URL + `/webhook` as your Twilio sandbox webhook.

---

## 🔑 API Keys (All Free)

| Service | Purpose | Get it |
|---|---|---|
| Twilio | WhatsApp messaging | [twilio.com](https://twilio.com) |
| Groq | AI + Voice transcription | [console.groq.com](https://console.groq.com) |

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10 |
| Web Framework | FastAPI (async) |
| WhatsApp | Twilio API (Meta Cloud API compatible) |
| AI | Groq (LLaMA 3.1) |
| Voice-to-text | Groq Whisper |
| Vector Search | ChromaDB + sentence-transformers |
| Memory | Redis (with automatic fallback) |

---

## 📦 Per Client Customization

Update `config.py`:
```python
COMPANY_NAME = "Client Business Name"
AGENT_NAME = "Assistant Name"
```

Drop their documents into `knowledge/` — that's it.

---

## 📄 License

MIT License

## 👨‍💻 Author

**Usman Javaid** — [@usmanxjavaid](https://github.com/usmanxjavaid)