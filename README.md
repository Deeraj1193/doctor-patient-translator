# 🏥 Doctor–Patient AI Translation Web Application

A full stack healthcare communication platform that enables real time multilingual interaction between doctors and patients using AI translation, voice notes, search option and chat summarization.

---

## 🚀 Project Overview

This application acts as a real time translation bridge between a doctor and a patient. It supports:

- Multilingual text translation
- Voice message recording and playback
- Persistent conversation logging
- Keyword based conversation search
- Chat summarization

The system is designed to simulate a clinical consultation scenario where language barriers exist.

---

## 🎯 Core Features Implemented

### Real-Time Doctor–Patient Translation
- Two roles: Doctor and Patient
- Text messages translated instantly using HuggingFace-hosted LLM
- Supports multiple languages

---

### Text Chat Interface
- Clean and Simple Chat UI
- Role-based message alignment
- Timestamped messages
- Translation shown below original message

---

### Audio Recording & Storage
- In browser voice recording
- Audio saved in backend
- Audio playback inside chat bubble
- Audio files stored server side

---

### Conversation Logging
- SQLite database
- Messages stored with:
  - Role
  - Original text
  - Translated text
  - Audio path - for voice recorded messages
  - Timestamp
- Conversation persists across page refresh

---

### Conversation Search
- Keyword based search
- Matches across conversation history
- Filtered results displayed dynamically

---

### AI Chat Summary
- Generates concise structured chat summary
- Removed dialogue format

---

## AI Integration

The system integrates with:

**HuggingFace Inference Router**
- Model: `mistralai/Mistral-7B-Instruct-v0.2`
- Used for:
  - Language translation
  - Medical conversation summarization

Design Decisions:
- Chosen for free-tier accessibility
- Simple REST-based integration
- Lightweight and fast enough for demo use

---

## Architecture

```

Frontend (React + Vite)
↓
REST API (FastAPI Backend)
↓
SQLite Database
↓
HuggingFace LLM API

```

---

## Tech Stack

### Frontend
- React 
- CSS 
- Fetch API

### Backend
- FastAPI
- SQLAlchemy
- SQLite
- Python-dotenv
- Requests

### AI
- HuggingFace LLM (Mistral 7B Instruct)

---

## Development Tools & Resources

### AI Tools
- ChatGPT

### Resources used
- HuggingFace Documentation : https://huggingface.co/docs

---

## Project Structure

```

doctor-patient-translator/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── services/
│   │   └── main.py
│   ├── requirements.txt
│   └── translator.db
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   └── App.jsx
│   └── index.html
│
└── README.md

```

---

## Setup Instructions

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
````

---

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## Environment Variables

Create `.env` inside backend folder:

```
HF_API_TOKEN=your_huggingface_token
```

---

## Known Limitations

* Audio transcription is not implemented (audio stored and played back only)
* SQLite used for demo simplicity (not production-grade scaling)
* No authentication implemented
* No multi-session chat threads (single session ID used)

---

## Future Improvements

* Whisper based speech to text transcription (for translating voice notes)
* Multi session support
* Role based authentication (proper conversation app)
* Production database (PostgreSQL)
* WebSocket based real time updates
* Token usage optimization
* Fine tune AI translation to be consistent and better

---

## Responsiveness

UI supports both desktop and mobile layouts with fixed bottom input bar and adaptive message bubbles.

---

## Evaluation Focus

This project demonstrates:

* Full-stack system architecture
* REST API design
* LLM integration
* Audio handling in browser
* Persistent storage
* Prompt engineering
* UI/UX design

---

## Author

Deeraj N
Full Stack Developer

```

---
