import os
from dotenv import load_dotenv
from modules.audio import record_audio
from modules.home_assistant import send_audio_to_hass, call_hass_conversation

load_dotenv()

def main():
    print("=== Voice-to-HomeAssistant Assistant ===")
    
    # 1. Enregistrement audio sur le Chromebook
    audio_path = record_audio("command.wav")
    
    if audio_path:
        print("\n[STEP 2] Envoi à Home Assistant...")
        
        # Option A: Envoyer l'audio pour transcription (si Whisper est configuré sur HA)
        texte = send_audio_to_hass(audio_path)
        
        if texte:
            print(f"HA a compris : {texte}")
            
            # Option B: Envoyer le texte au cerveau (Assist/GPT) de HA
            reponse = call_hass_conversation(texte)
            
            if reponse:
                print("\n" + "="*30)
                print(f"RÉPONSE HA : {reponse}")
                print("="*30 + "\n")
        else:
            print("[ERROR] Home Assistant n'a pas pu transcrire l'audio.")
    else:
        print("[ERROR] Échec de l'enregistrement.")

if __name__ == "__main__":
    if not os.getenv("HASS_TOKEN"):
        print("[CRITICAL] Erreur : HASS_TOKEN non trouvé dans .env")
    else:
        main()
