from core import classificador
from core import util
import unicodedata

class Chatbot():
    def __init__(self):
        pass

    def interagir(self, entrada):
        cl=classificador.Classificador()
        texto=cl.normalizar(entrada)
        resposta = "Desculpe, não tenho resposta para isso"
        re=False
        #texto = cl.to_ascii(texto) caso precise tirar os acentos
        print(texto)
        arq = util.Arquivo()
        inputs=arq.lertudo("/BD/txt/i.txt")
        outputs=arq.lertudo("/BD/txt/o.txt")

        n=0


        for i in inputs:
            if (texto+"\n" == i):
                resposta=unicodedata.normalize("NFD",outputs[n])
                re=True
                return resposta,re
            n+=1
        return resposta,re
    
    def aprender1(self,entrada):
        v=util.Voz()
        cl=classificador.Classificador()

        v.speak("Você quer cadastrar uma?")
        saida=v.escute()
        print("Passou do escute")
        
        saida=cl.normalizar(saida)
        sim=["sim","claro","com certeza","óbvio que sim","por favor","correto","afirmativo"]
        for i in sim:
            if saida in i:
                while True:
                    v.speak("Qual é a resposta?")
                    saida=v.escute()

                    v.speak("Então a sua entrada é:, "+entrada)
                    v.speak("E a sua saída é:, "+saida)
                    v.speak("Correto?")
                    resp=v.escute()

                    for i in sim:
                        if resp in i:
                            v.speak("Ok, gravando resposta")

                            entrada = cl.normalizar(entrada)
                            saida=cl.normalizar(saida)

                            arq=util.Arquivo()
                            arq.gravar("/BD/txt/i.txt",entrada)
                            arq.gravar("/BD/txt/o.txt",saida)

                            return

                        v.speak("Você pode repetir por favor?")
                        v.speak("Qual é a pergunta?")
                        entrada=v.escute()
        v.speak("Ok, fica para a próxima")
        return
                