import os
import time
import speech_recognition as sr
import pyttsx3
import core

ld = core.Load()
info = ld.carregar()
ld.iniciar(info)
class Arquivo():
    
    def __init__(self):
        pass

    def lertudo(self,complemento="res/infos.txt"):
        
        os.chdir(r'C:/Users/lucas/Documents/Serena/serena/')
        caminho=os.getcwd()+complemento

        arq = open(caminho, 'r',encoding="utf8")
        info=arq.readlines()
        arq.close()

        return info

    def gravar(self,caminho, texto):
        os.chdir(r'C:/Users/lucas/Documents/Serena/serena/')
        cc = os.getcwd()+caminho

        arq = open(cc,'r+',encoding="utf8")
        arq.readlines()
        arq.write(texto+"\n")
        arq.close()

class Voz():
    def __init__(self):
        pass
    def speak(self,text):
        self.delay=len(text)
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        print(voices)
        engine.setProperty('voice',voices[-2].id)
        engine.say(text)
        engine.runAndWait()
        time.sleep(0.08*self.delay)
        
        
        return

    def escute(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Pode falar:")
            audio = r.listen(source)
            result= r.recognize_google(audio, language="pt-BR")
            sair=['sair','encerrar','fechar','dormir','boa noite','adeus','até mais','finalizar']
            hora=['horas','horário','hora']
            n=0       
            for i in sair:
                for e in hora:
                    if(result in i):
                        self.speak("Até mais "+ ld.nomeUsu)
                        print("Programa encerrado")
                        exit()
                    if(result in e):
                         saida = core.SystemInfo.get_time()
                         n+=1
            return result