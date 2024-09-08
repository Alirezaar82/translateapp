from tkinter import *
from deep_translator import GoogleTranslator


def translate_text():
    text = input_text.get("1.0", END)  
    translated = GoogleTranslator(source='auto', target='en').translate(text)
    output_text.delete("1.0", END)  
    output_text.insert(END, translated)  

root = Tk()
root.title("Text Translator")
root.geometry("400x300")


input_label = Label(root, text="Enter text to translate (in any language):")
input_label.pack(pady=10)


input_text = Text(root, height=5, width=40)
input_text.pack(pady=10)


translate_button = Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)


output_text = Text(root, height=5, width=40)
output_text.pack(pady=10)


root.mainloop()

