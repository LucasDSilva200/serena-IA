import unidecode

class Classificador():
    def __init__(self):
        pass

    def fatiar(self,frase):
        palavras=frase.split(" ")
        return palavras
        
    def normalizar(self,frase):
        frase=frase.lower()
        return frase
    
    def aprende(self,listadetreino):
        listadetreino

    def to_ascii(self,ls):
        ascii=unidecode.unidecode(ls)
        return ascii
