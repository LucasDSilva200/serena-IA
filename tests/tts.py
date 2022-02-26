import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[-2].id)
engine.say("Eu vou falar esse texto")
engine.runAndWait()
'''from multiprocessing.dummy import Pool
from vosk import Model, KaldiRecognizer

import sys
import os
import wave
import json

model = Model('model')

def recognize(line):
    uid, fn = line.split()
    wf = wave.open(fn, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())

    text = ""
    while True:
        data = wf.readframes(1000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            jres = json.loads(rec.Result())
            text = text + " " + jres['text']
    jres = json.loads(rec.FinalResult())
    text = text + " " + jres['text']
    return (uid + text)

def main():
    p = Pool(8)
    texts = p.map(recognize, open(sys.argv[1]).readlines())
    print ("\n".join(texts))

main()'''