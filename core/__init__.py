import os
import datetime
import PySimpleGUI as sg


class SystemInfo:
    def __init__(self) -> None:
        pass
    def get_time():
        now = datetime.datetime.now()
        answer = 'São {} horas e {} minutos.'.format(now.hour,now.minute)
        return answer    
    def get_hour():
        now = datetime.datetime.now()
        if now.hour >= 5:
            answer = 'Bom dia'
        if now.hour >= 12:
            answer = 'Boa tarde'
        if now.hour >= 18:
            answer = 'Boa noite'
        return answer    

class Load():
    def __init__(self) -> None:
        sg.theme('DarkTeal12')
        layout = [
            [sg.Text('Como devo lhe chamar',size=(20,1))],
            [sg.Input(key='user',size=(20,1))],
            [sg.Text('Nome da IA',size=(20,1))],
            [sg.Input(key='ia',size=(20,1))],
            [sg.Button('Ok',size=(20,1))]
        ]
        self.janela=sg.Window('Bem-vindo',layout)
    
    def event(self):
        while True:
            event,values = self.janela.read()
            if event == sg.WIN_CLOSED:
                break
            if event =='Ok':
                self.janela.close()
                return values['user'],values['ia']
    
    def carregar(self):
        c1=os.chdir(r'C:/Users/lucas/Documents/Serena/serena/res')#Aponta para o caminho do arquivo
        caminho=os.getcwd()+"/infos.txt"#Monta o caminho do txt infos
        print(caminho)
        arq = open(caminho, 'r')
        info = arq.readlines()
        
        arq.close()
        return info
    def iniciar(self,info):
        self.nomeUsu = info[0]
        self.nomeIa = info[1]
        self.first = str(info[2])
        aux=""
        for i in self.nomeIa:
            if i== " ":
                break
            else:
                aux=aux+i
        self.nomeIa=aux
        if(("0"in self.first)or ("User"in self.nomeUsu)):
            valUsr,valIA = self.event()
            self.nomeUsu = valUsr 
            self.nomeIa = valIA
            os.chdir(r'C:/Users/lucas/Documents/Serena/serena/res')
            caminho=os.getcwd()+"/infos.txt"
            arq = open(caminho, 'w')
            info = arq.writelines(self.nomeUsu+"\n"+self.nomeIa+"\n"+"1 \n")
            arq.close()
        return
