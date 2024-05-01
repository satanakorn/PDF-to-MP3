from gtts import gTTS
from PyPDF2 import PdfReader

def pdf_to_text(pdf_file):
    text = ''
    with open(pdf_file, 'rb') as f:
        reader = PdfReader(f)
        for i in range(len(reader.pages)):
            page = reader.pages[i]
            text = text + page.extract_text()
    return text

def text_to_audio(text , output_file):
    tts = gTTS(text)
    tts.save(output_file)


pdf_file = "example.pdf"
output_audio_file = "audio_example.mp3"

text = pdf_to_text(pdf_file)
text_to_audio(text, output_audio_file)