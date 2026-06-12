import os
from openai import OpenAI
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configuration OpenAI (pour Whisper STT)
client_openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Configuration Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def transcribe_audio(file_path):
    """Transforme l'audio en texte via OpenAI Whisper."""
    try:
        with open(file_path, "rb") as audio_file:
            transcript = client_openai.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file
            )
        return transcript.text
    except Exception as e:
        print(f"[ERROR] Erreur Transcription : {e}")
        return None

def get_gemini_response(prompt):
    """Envoie le texte à Gemini et récupère la réponse."""
    try:
        response = model.generate_content(f"Tu es un assistant domotique vocal concis. Réponds en une phrase courte : {prompt}")
        return response.text
    except Exception as e:
        print(f"[ERROR] Erreur Gemini : {e}")
        return None
