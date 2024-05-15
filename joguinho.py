from tkinter import *
import random

LARGURA_JOGO = 1000
ALTURA_JOGO = 700
VELOCIDADE = 100
TAMANHO_ESPACO = 50
PARTES_CORPO = 3
COR_COBRA = "#00FF00"
COR_COMIDA = "#FF0000"
COR_FUNDO = "#000000"

fim_de_jogo = 0

class Cobra:

    def __init__(self):
        self.tamanho_corpo = PARTES_CORPO
        self.coordenadas = []
        self.quadrados = []

        for i in range(0, PARTES_CORPO):
            self.coordenadas.append([0, 0])

        for x, y in self.coordenadas:
            quadrado = canvas.create_rectangle(x, y, x + TAMANHO_ESPACO, y + TAMANHO_ESPACO, fill=COR_COBRA, tag="cobra")
            self.quadrados.append(quadrado)

class Comida:
    def __init__(self):

        x = random.randint(0, (LARGURA_JOGO // TAMANHO_ESPACO) - 1) * TAMANHO_ESPACO
        y = random.randint(0, (ALTURA_JOGO // TAMANHO_ESPACO) - 1) * TAMANHO_ESPACO

        self.coordenadas = [x, y]

        canvas.create_oval(x, y, x + TAMANHO_ESPACO, y + TAMANHO_ESPACO, fill=COR_COMIDA, tag="comida")


def proximo_turno(cobra, comida):
    
    x, y = cobra.coordenadas[0]

    if direcao == "cima":
        y -= TAMANHO_ESPACO
    if direcao == "baixo":
        y += TAMANHO_ESPACO
    if direcao == "esquerda":
        x -= TAMANHO_ESPACO
    if direcao == "direita":
        x += TAMANHO_ESPACO

    cobra.coordenadas.insert(0, (x, y))

    quadrado = canvas.create_rectangle(x, y, x + TAMANHO_ESPACO, y + TAMANHO_ESPACO, fill=COR_COBRA)

    cobra.quadrados.insert(0, quadrado)

    if x == comida.coordenadas[0] and y == comida.coordenadas[1]:

        global pontuacao
        pontuacao += 1

        label.config(text="Pontuação:{}".format(pontuacao))

        canvas.delete("comida")

        comida = Comida()

    else:

        del cobra.coordenadas[-1]

        canvas.delete(cobra.quadrados[-1])

        del cobra.quadrados[-1]

    if verificar_colisoes(cobra):
        fim_de_jogo()

    else:
        window.after(VELOCIDADE, proximo_turno, cobra, comida)

def mudar_direcao(nova_direcao):
    
    global direcao

    if nova_direcao == 'esquerda':
        if direcao != 'direita':
            direcao = nova_direcao
    elif nova_direcao == 'direita':
        if direcao != 'esquerda':
            direcao = nova_direcao
    elif nova_direcao == 'cima':
        if direcao != 'baixo':
            direcao = nova_direcao
    elif nova_direcao == 'baixo':
        if direcao != 'cima':
            direcao = nova_direcao

def verificar_colisoes(cobra):
    
    x, y = cobra.coordenadas[0]

    if x < 0 or x >= LARGURA_JOGO:
        return True
    elif y < 0 or y >= ALTURA_JOGO:
        return True

    for parte_corpo in cobra.coordenadas[1:]:
        if x == parte_corpo[0] and y == parte_corpo[1]:
            return True
        
    return False

def fim_de_jogo():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('arial', 70), text="FIM DE JOGO", fill="red", tag="fim_de_jogo")
    global fim_de_jogo
    fim_de_jogo = 1

def reiniciar_jogo():

    global fim_de_jogo
    if fim_de_jogo == 1:
        fim_de_jogo = 0
        global cobra
        global canvas
        canvas.delete(ALL)

        global direcao
        direcao = "baixo"

        global pontuacao
        pontuacao = 0
        label.config(text="Pontuação:{}".format(pontuacao))

        cobra = Cobra()
        
        global comida
        comida = Comida()

        window.update()

        proximo_turno(cobra, comida)

window = Tk()
window.title("Jogo da Cobra")
window.resizable(False, False)

pontuacao = 0
direcao = "baixo"

label = Label(window, text="Pontuação:{}".format(pontuacao), font=("arial", 30))
label.pack()

canvas = Canvas(window, bg=COR_FUNDO, height=ALTURA_JOGO, width=LARGURA_JOGO)
canvas.pack()

window.update()

largura_janela = window.winfo_width()
altura_janela = window.winfo_height()
largura_tela = window.winfo_screenwidth()
altura_tela = window.winfo_screenheight()


x = int((largura_tela/2) - (largura_janela/2))
y = int((altura_tela/2) - (altura_janela/2))

window.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

window.bind('<Left>', lambda event: mudar_direcao("esquerda"))
window.bind('<Right>', lambda event: mudar_direcao("direita"))
window.bind('<Up>', lambda event: mudar_direcao("cima"))
window.bind('<Down>', lambda event: mudar_direcao("baixo"))
window.bind('<space>', lambda event: reiniciar_jogo())

cobra = Cobra()
comida = Comida()

proximo_turno(cobra, comida)

window.mainloop()
