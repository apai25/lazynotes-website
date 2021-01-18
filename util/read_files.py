import speech_recognition as sr
from PIL import Image
import pytesseract

def audio_to_string(audio_path):

    r = sr.Recognizer()
    audio_file = sr.AudioFile(audio_path)

    with audio_file as source:
        audio = r.record(source)
    
    text = r.recognize_google(audio)
    return text

def text_to_string(path):

    with open(path, 'r') as file:
        data = file.read().replace('\n', '')
    
    return data

def image_to_string(path):
    image = Image.open(path)

    data = pytesseract.image_to_string(image)
    return data
