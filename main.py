from tkinter import *
from deep_translator import GoogleTranslator
import speech_recognition as sr


def translate_text(text):
    output_text.insert(END, 'در حال ترجمه...\n')
    translated = GoogleTranslator(source='auto', target='en').translate(text)
    return translated


def get_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    MicText = r.recognize_google(audio, language='fa-IR')
    return MicText


def listen_and_translate():
    try:
        text = get_text()
        output_text.insert(END, f"متن دریافت شده: {text}\n")

        translated_text = translate_text(text)
        output_text.insert(END, f"ترجمه: {translated_text}\n")
    except Exception as e:
        output_text.insert(END, f"خطا: {str(e)}\n")


root = Tk()
root.title("Voice to Text Translator")
root.geometry("400x300")


listen_button = Button(root, text="Listen & Translate", command=listen_and_translate)
listen_button.pack(pady=20)


output_text = Text(root, height=10, width=50)
output_text.pack(pady=10)


root.mainloop()
