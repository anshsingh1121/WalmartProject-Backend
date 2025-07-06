# WalmartProject-Backend 🎧📝

![Python](https://img.shields.io/badge/python-3.8%2B-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-async--framework-green) ![Whisper](https://img.shields.io/badge/Whisper-OpenAI-blueviolet) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This is the **backend** for the **WalmartProject** — an AI-powered application that allows users to upload audio files and receive transcribed text in real-time using **OpenAI's Whisper** model. It is built with **FastAPI** and integrates Whisper for accurate speech-to-text conversion.

## 🚀 Features

- 🎤 Upload and transcribe audio (MP3, WAV, etc.)
- 🧠 Uses Whisper AI (`base` model) for transcription
- ⚡ Built with FastAPI — fast, async, and modern Python API framework
- 📁 Clean file handling and simple structure
- 🧪 Interactive Swagger UI for API testing
- 🔄 Auto-reload for development using Uvicorn
- 📦 Easy deployment to Render / Railway / Docker

## 🧰 Tech Stack

- **Language**: Python 3.8+
- **Framework**: FastAPI
- **ASGI Server**: Uvicorn
- **AI Model**: Whisper (OpenAI)
- **Deployment**: Render / Railway / Docker (optional)

## 📂 Project Structure

```text
WalmartProject-Backend/
├── whispertranscribe.py   # Core logic to transcribe audio
├── main.py                # FastAPI app with routes
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
```

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/anshsingh1121/WalmartProject-Backend.git
cd WalmartProject-Backend
```

### 2. Create a virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have `requirements.txt`, install manually:

```bash
pip install fastapi uvicorn openai-whisper
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

Access Swagger UI at: http://127.0.0.1:8000/docs

## 📤 API Endpoint

### `POST /transcribe`

Transcribes the uploaded audio file using Whisper.

- **Form field**: `file`
- **Content-Type**: `multipart/form-data`

Example using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/transcribe" -F "file=@sample.mp3"
```

Response:

```json
{
  "transcription": "This is the transcribed text from the audio."
}
```

## 🚀 Deployment

### 🟢 Deploy to Render

1. Push your code to GitHub
2. Go to https://render.com
3. Create a new **Web Service**
4. Set:
   - **Environment**: Python 3
   - **Start Command**: `uvicorn main:app --host=0.0.0.0 --port=10000`
5. Add `requirements.txt` and deploy

### 🐳 Docker Deployment (optional)

```dockerfile
# Dockerfile
FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build & run:

```bash
docker build -t walmart-backend .
docker run -p 8000:8000 walmart-backend
```

## ✅ To Do

- Add multi-language support
- Add API key authentication
- Add support for different Whisper model sizes
- Store transcriptions in a database
- Add logging and better error handling

## 📜 License

This project is licensed under the **MIT License**. See the LICENSE file for details.

## 🙋‍♂️ Author

**Ansh Singh**  
🔗 [GitHub](https://github.com/anshsingh1121)

Built with 💡 and 🎧 using Whisper AI and FastAPI
