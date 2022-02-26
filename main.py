import speech_recognition as sr
import core
from core import chatbot
from core import util


#criar um reconhecedor
r = sr.Recognizer()
#---------------------

#inicia a classe load

ld=core.Load()
utilVoz=util.Voz()
info = ld.carregar()#faz com que o programa só leia a primeira linha
ld.iniciar(info)
ch=chatbot.Chatbot()
#--------------------


#sintese de fala
#---------------

#mudando a voz da IA

#-------------------

#método de fala

#---------------

#Abrir microfone para a captura
time = core.SystemInfo.get_hour()
utilVoz.speak(time+ld.nomeUsu)

while True:
    try:
        texto1 = utilVoz.escute()
        print(texto1)
        
        if ld.nomeIa in texto1 + "\n":
            utilVoz.speak("Olá meu nome é " + ld.nomeIa)
            break
    except sr.UnknownValueError:
        print("fale algo")
        continue

while True:
    try:
        #Transforma a fala em texto
        texto = utilVoz.escute()
        #--------------------------
        #verificação de texto

        saida=ch.interagir(texto)                   
        utilVoz.speak(saida[0])

        if saida[1]==False:
            ch.aprender1(texto)
            
    except sr.UnknownValueError:
        print("Fale algo")
        continue
