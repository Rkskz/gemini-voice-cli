# Gemini Voice CLI

Voice assistant powered by Gemini and Home Assistant, running on a Chromebook (simulating ESP32 hardware).

## Architecture
1. **Input:** Local microphone recording.
2. **STT:** Cloud-based Speech-to-Text.
3. **Processing:** Gemini/GPT-4o mini via Home Assistant.
4. **TTS:** Cloud-based Text-to-Speech.
5. **Output:** Google Nest via Google Cast.
