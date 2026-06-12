import os
from dotenv import load_dotenv
from modules.audio import record_audio
from modules.gemini_client import process_voice_command

# Chargement des variables d'environnement
load_dotenv()

def main():
    print("=== Gemini Voice Assistant (Chromebook Edition) ===")
    
    # 1. Enregistrement audio
    audio_path = record_audio("command.wav")
    
    if audio_path:
        print("\n[STEP 2] Analyse en cours via Gemini...")
        
        # 2. Envoi à Gemini (Analyse audio + Réflexion)
        reponse = process_voice_command(audio_path)
        
        if reponse:
            print("\n" + "="*30)
            print(f"ASSISTANT : {reponse}")
            print("="*30 + "\n")
        else:
            print("[ERROR] Gemini n'a pas pu traiter la demande.")
    else:
        print("[ERROR] Échec de l'enregistrement.")

if __name__ == "__main__":
    if not os.getenv("GEMINI_API_KEY"):
        print("[CRITICAL] Erreur : GEMINI_API_KEY non trouvée dans le fichier .env")
    else:
        main()
