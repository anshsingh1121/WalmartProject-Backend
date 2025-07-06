from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from whisper_transcribe import transcribe_audio
import shutil
import os
from pathlib import Path

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    upload_dir = Path("uploads")
    upload_dir.mkdir(parents=True, exist_ok=True)

    filepath = upload_dir / file.filename

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = transcribe_audio(str(filepath.resolve()))  # pass full absolute path
    print(f"Transcript: {text[:100]}...")
    return {"transcript": text}


@app.get("/")
def root():
    return {"message": "SnapSound backend is running 🚀"}
