import speech_recognition as sr
import os

def record_audio(filename="input.wav"):
    """
    Records audio from the microphone until silence is detected.
    Returns the path to the recorded file.
    """
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\n[INFO] Écoute... (parle maintenant)")
        # Ajuste le niveau de bruit ambiant pour une meilleure détection
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        try:
            # Enregistre jusqu'à ce qu'un silence soit détecté
            audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=15)
            
            with open(filename, "wb") as f:
                f.write(audio_data.get_wav_data())
            
            print(f"[SUCCESS] Audio enregistré : {filename}")
            return filename
            
        except sr.WaitTimeoutError:
            print("[ERROR] Timeout : Aucune parole détectée.")
            return None
        except Exception as e:
            print(f"[ERROR] Erreur lors de l'enregistrement : {e}")
            return None

def play_audio(file_path):
    # TODO: Implémenter la lecture audio si nécessaire (plus tard via Google Nest)
    pass
