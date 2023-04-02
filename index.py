import speech_recognition as sr 
import pyaudio
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Menginisialisasi recognizer
r = sr.Recognizer()

# Menggunakan microphone sebagai input
with sr.Microphone() as source:
    print("Mulai Berbicara :")
    audio = r.listen(source)

    try:
        print("Anda Berkata: " + r.recognize_google(audio))
        
    # Error handling ketika speech recognition gagal 
    except sr.UnknownValueError:
        print("Speech Recognition gagal untuk mengenali suara")
        
    except sr.RequestError as e:
        print("Speech Recognition service error: {0}".format(e))
