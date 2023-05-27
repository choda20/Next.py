import gtts
from playsound import playsound

if __name__ == "__main__":
    speech = gtts.gTTS(text = "first time i'm using a package in next.py course", lang="en")
    speech.save('TTS-Audio.mp3')
    playsound('TTS-Audio.mp3')