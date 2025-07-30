# LLM-Real-Time-Translation-and-mic-speaking

This project is a real-time translator using Meta's NLLB-200 language model, integrated with Python. It uses LLM inference on CPU via the llama.cpp library (or similar), making it lightweight and easy to run locally.

The system captures your voice through the microphone in your native language and translates it into another language. By default, it is set up to translate Brazilian Portuguese to English.

⚙️ Features
🎙️ Captures real-time speech using your default Windows microphone

🌍 Translates to over 200 languages using the NLLB-200 model

🧠 Uses a fine-tuned version of the NLLB-200 model for better performance with Portuguese

💬 Speaks back the translated text using TTS (Text-to-Speech)

🚀 How to Run
Clone this Repository:
git clone https://github.com/AlysonSanto/LLM-Real-Time-Translation-and-mic-speaking.git

Run: 

pip install -r requirements.txt
python Download.py (to take the model from Google Drive)

Run the program:
python AI_voice.py

The script will:
Listen to your microphone (in Brazilian Portuguese)
Translate what you say into English
Speak the translated text using your default TTS voice

🔧 Notes
The translation model (nllb-200-distilled-600M) used here is fine-tuned specifically for Portuguese translations.

This may lead to lower translation quality for other language pairs.


📣 Disclaimer
This is a personal/hobby project. Performance depends on your hardware (CPU and mic quality) and the model version used. Feel free to fork, improve, or adapt it to other languages.
