import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Configuration OpenAI unique
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def transcribe_audio(file_path):
    """Transforme l'audio en texte via OpenAI Whisper."""
    try:
        with open(file_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file
            )
        return transcript.text
    except Exception as e:
        print(f"[ERROR] Erreur Transcription Whisper : {e}")
        return None

def get_llm_response(prompt):
    """Envoie le texte à GPT-4o mini et récupère la réponse."""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Tu es un assistant domotique vocal. Réponds de façon très concise (une phrase)."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"[ERROR] Erreur GPT-4o mini : {e}")
        return None
