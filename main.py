from tkinter import *
from deep_translator import GoogleTranslator
import speech_recognition as sr
import pyttsx3 as tts



def translate_text(text):
    output_text.insert(END, 'در حال ترجمه...\n')
    translated = GoogleTranslator(source='auto', target='en').translate(text)
    return translated


def get_text():
    output_text.insert(END, 'در حال گوش دادن...\n')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    MicText = r.recognize_google(audio, language='fa-IR')
    output_text.insert(END, f"متن دریافت شده: {MicText}\n")
    return MicText


def TTS(translate_text):
    output_text.insert(END, 'در حال پخش...\n')
    engine = tts.init()
    engine.say(translate_text)
    engine.runAndWait()


def listen_translate_and_speak():
    try:
        
        text = get_text()

        
        translated_text = translate_text(text)

        
        if var.get() == 1:  
            TTS(translated_text)
        else:
            output_text.insert(END, f"ترجمه: {translated_text}\n")
    except Exception as e:
        output_text.insert(END, f"خطا: {str(e)}\n")


root = Tk()
root.title("Voice to Text Translator with TTS")
root.geometry("400x350")


listen_button = Button(root, text="Listen & Translate", command=listen_translate_and_speak)
listen_button.pack(pady=20)


var = IntVar()
checkbox = Checkbutton(root, text="Listen to the translation", variable=var)
checkbox.pack(pady=5)


output_text = Text(root, height=10, width=50)
output_text.pack(pady=10)

root.mainloop()
