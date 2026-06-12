import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configuration Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def process_voice_command(audio_path):
    """
    Envoie l'audio directement à Gemini pour analyse et réponse.
    C'est gratuit et ça fait STT + LLM en un seul appel !
    """
    try:
        # 1. Upload du fichier audio vers Google
        audio_file = genai.upload_file(path=audio_path)
        
        # 2. Demander à Gemini d'analyser l'audio
        response = model.generate_content([
            "Tu es un assistant domotique vocal. Écoute cet audio et réponds de manière très concise (une phrase courte).",
            audio_file
        ])
        
        return response.text
    except Exception as e:
        print(f"[ERROR] Erreur Gemini Voice : {e}")
        return None
