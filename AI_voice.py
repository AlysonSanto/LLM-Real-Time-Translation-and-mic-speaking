import speech_recognition as sr
import pyttsx3
import ctranslate2
from transformers import AutoTokenizer
import transformers


# Inicializar TTS
tts = pyttsx3.init()
tts.setProperty("rate", 230)  

def traduzir(padrao):
    src_lang = "por_Latn"
    tgt_lang = "eng_Latn"

    translator = ctranslate2.Translator("nllb-200-distilled-600M")
    tokenizer = transformers.AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M", src_lang=src_lang)

    source = tokenizer.convert_ids_to_tokens(tokenizer.encode(padrao))
    target_prefix = [tgt_lang]
    results = translator.translate_batch([source], target_prefix=[target_prefix])
    target = results[0].hypotheses[0][1:]

    resultado = tokenizer.decode(tokenizer.convert_tokens_to_ids(target))

    return resultado

# Função para ouvir o microfone
def ouvir_microfone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Fale algo em português...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("⏰ Ninguém falou a tempo.")
            return None

    try:
        texto = recognizer.recognize_google(audio, language="pt-BR")
        print(f"🗣️ Você disse: {texto}")
        return texto
    except sr.UnknownValueError:
        print("❓ Não entendi o que você disse.")
    except sr.RequestError:
        print("🚫 Erro ao se conectar ao serviço de reconhecimento.")
    return None

# Loop principal
while True:
    texto_pt = ouvir_microfone()
    if texto_pt:
        texto_en = traduzir(texto_pt)
        print(f"Tradução: {texto_en}")
        tts.say(texto_en)
        tts.runAndWait()
