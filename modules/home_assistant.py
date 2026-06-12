import os
import requests
from dotenv import load_dotenv

load_dotenv()

HASS_URL = os.getenv("HASS_URL")
HASS_TOKEN = os.getenv("HASS_TOKEN")

def send_audio_to_hass(audio_path):
    """
    Envoie le fichier audio à Home Assistant via l'API Assist (STT + LLM + Action).
    """
    url = f"{HASS_URL}/api/stt/stt.openai_whisper" # Exemple avec l'add-on Whisper
    
    # Note: Home Assistant utilise souvent une WebSocket ou un endpoint spécifique pour Assist.
    # Pour simplifier, on va d'abord viser l'endpoint de transcription ou une automation.
    
    headers = {
        "Authorization": f"Bearer {HASS_TOKEN}",
    }
    
    try:
        with open(audio_path, "rb") as f:
            # Envoi du fichier audio (format WAV)
            response = requests.post(
                f"{HASS_URL}/api/stt/whisper", # À adapter selon l'add-on installé
                headers=headers,
                data=f
            )
        
        if response.status_code == 200:
            return response.json().get("text")
        else:
            print(f"[ERROR] Home Assistant STT Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"[ERROR] Connection to Home Assistant failed: {e}")
        return None

def call_hass_conversation(text):
    """
    Envoie du texte à l'agent de conversation de Home Assistant.
    """
    url = f"{HASS_URL}/api/conversation/process"
    headers = {
        "Authorization": f"Bearer {HASS_TOKEN}",
        "Content-Type": "application/json",
    }
    data = {
        "text": text,
        "language": "fr"
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()["response"]["speech"]["plain"]["speech"]
        else:
            print(f"[ERROR] Home Assistant Conversation Error: {response.text}")
            return None
    except Exception as e:
        print(f"[ERROR] Conversation failed: {e}")
        return None
