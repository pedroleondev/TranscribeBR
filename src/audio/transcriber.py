import os
import subprocess
import whisper
import torch
from dotenv import load_dotenv

load_dotenv()

def transcribe_audio(wav_file_path: str) -> str:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisper.load_model("small", device=device)

    common_args = {
        "language": "pt",
        "task": "transcribe",
        "temperature": 0,
        "verbose": True
    }

    try:
        print("Transcribing with fp16=True")
        result = model.transcribe(wav_file_path, fp16=True, **common_args)
    except RuntimeError as e:
        print(f"Error with fp16=True: {e}. Trying fp16=False...")
        result = model.transcribe(wav_file_path, fp16=False, **common_args)

    return result.get("text", "")