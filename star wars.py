import time
import turtle
import random
import winsound


'''
Trabalho de Fundamentos da Programação do 
curso Ciência da Computação - Universidade Federal do Ceará

Aluno: Yvens Almeida Girão
Matrícula: 542481

Link do Vídeo no youtube: https://youtu.be/0hn-nau79MA

'''

winsound.PlaySound("swt.wav", winsound.SND_ASYNC)  # Importando som do Menu Principal


# Janela
tela = turtle.Screen()              # Cria a variável "tela"
tela.setup(1024, 600)               # Altura e largura da Janela
tela.bgcolor('black')               # Cor interna da janela
tela.bgpic('logo.gif')              # Imagem do Menu Principal
tela.title('STAR WARS')             # Nome da Janela
tela.tracer(0)
# Adicinando skins
tela.addshape('millennium.gif')     # Adicionando o gif do personagem
tela.addshape('asteroide.gif')      # Adicionando o gif dos inimigos   
tela.addshape('yoda.gif')           # Adicionando o gif do combustível
tela.addshape('logo.gif')           # Adicionando o gif do Menu Principal


# Arena
arena = turtle.Turtle()             # Criando variavel arena
arena.speed(0)                      # Velocidade da criação da borda
arena.color('white')                # Cor da borda
arena.hideturtle()                  # Escondendo a seta
arena.width(7)                      # Espressura da borda
arena.penup()                       # Não riscar quando:
arena.goto(-300, -295)                          # For para essas coordenadas
arena.shapesize(1)                  # Tamanho da seta (Não será considerado, pois o comando hideturtle escondeu a seta)
arena.pendown()                     # Faz com que a caneta comece a riscar para formar a borda
for i in range(4):                  # Faz com que ela repita os comandos dentro desse laço 4 vezes
    arena.forward(600)
    arena.left(90)


#personagem

personagem = turtle.Turtle()           # Variavel personagem
personagem.shape('millennium.gif')     # Skin do personagem
personagem.penup()                     # Não riscar a tela
personagem.speed(0)                    # Não mostrar animação
personagem.color('white')              # Cor da seta(Inútil, já tem a skin)
personagem.goto(0,-200)                # Manda o personagem para a coordenada X:0 Y:-200

estrelas = []

for i in range(7):
    estrela = turtle.Turtle()         # Variavel estrela
    estrela.speed(0)                  # Sem animação
    estrela.shapesize(0.2)            # Tamanho da estrela
    estrela.shape("circle")           # Formato da estrela
    estrela.color("white")            # Cor da estrela
    estrela.penup()                   # Não riscar a tela
    estrela.goto(-550, 250)           # Mandei para fora do plano quando fosse executada pela primeira vez
    estrela.speed = 3                 # Velocidade da estrela
    

    estrelas.append(estrela)

inimigos = []

for i in range(4):
    inimigo = turtle.Turtle()         # Variavel Inimigo
    inimigo.speed(0)                  # Desligar animação
    inimigo.shapesize(1)              # Tamanho
    inimigo.shape("asteroide.gif")    # Skin
    inimigo.color("red")              # Inutil, ja tem skin
    inimigo.penup()                   # Não riscar a tela
    inimigo.goto(-550, 250)           # Para fora do plano para não aparecer na tela pela primeira vez
    inimigo.speed = 1                 # Velocidade do inimigo
    

    inimigos.append(inimigo)



yodas = []

for i in range(1):
    yoda = turtle.Turtle()          # Variavel Yoda (COMBUSTIVEL)
    yoda.speed(0)                   # Desligar animação
    yoda.shapesize(3)               # Tamanho 
    yoda.shape('yoda.gif')          # Skin
    yoda.penup()                    # Não riscar a tela
    yoda.color('red')               # Cor se caso não tiver skin
    yoda.goto(-550, -290)           # Para fora do plano
    yoda.speed = 0.8                # Velocidade

    yodas.append(yoda)



def direita():                    # Função para ir Direita

    personagem.forward(30) 


def esquerda():                   # Função para ir a Esquerda

    personagem.backward(30) 




tela.onkeypress(direita,'Right')     # Função DIREITA irá ser chamada ao clicar o botão RIGHT do teclado
tela.onkeypress(esquerda,'Left')     # Função ESQUERDA irá ser chamada ao clicar no botão LEFT do teclado
tela.onkeypress(direita,'d')         # Função DIREITA irá ser chamada ao clicar o botão d do teclado
tela.onkeypress(esquerda,'a')        # Função ESQUERDA irá ser chamada ao clicar no botão a do teclado

tela.listen()                        # Espera comando do teclado para retratar nas funções 



def start():                                                # Função Para iniciar o jogo
    winsound.PlaySound("sabre.wav", winsound.SND_ASYNC)     # Adicionando som sabre de luz ao inicar jogo 
    score = 0    # Pontuação inicial
    combustivel = 50   # Combustivel Inicial
    while True:        # Laço Para repetir tudo que está identado
        tela.bgpic('black.gif')    # Fundo preto (adicionei skin)
        #Hud
        hud = turtle.Turtle()           #
        hud.speed(0)                      #
        hud.shape("square")                #
        hud.color("yellow")                 # Isso é para mostrar a Pontuação no lado esquerdo da tela
        hud.penup()                        #        
        hud.hideturtle()                  #  
        hud.goto(-410, 235)             #
        hud.write("Pontos: 0 \nCombustivel: 50%", align="center", font=("Arial", 18, "normal")) 

        while True:
            tela.update()               # Atualiza a tela
            
            if personagem.xcor() < -280 or personagem.xcor() > 280:    # Se caso tocar em uma das bordas
                winsound.PlaySound("explode.wav", winsound.SND_ASYNC)       # Som de explosão                                      
                combustivel -= 25                                           # -25% de combustivel
                personagem.setx(0)                                          # Manda para a posição inicial
                hud.clear()                                                 # Limpa antigo hud Para atualizar com o debaixo:
                hud.write(f"Pontos: {score} \nCombustivel: {combustivel}%", align="center", font=("Arial", 18, "normal"))
                        

            for estrela in estrelas:    
                # Move as estrelas
                estrela.sety(estrela.ycor() - estrela.speed)          # Manda estrelas para baixo
                if estrela.ycor() < -300:                             # Se passar desse ponto no Plano
                    estrela.goto(random.randint(-280, 280), random.randint(400, 800)) #Ela retorna para cima por causa do laço infinito
                    score += 1 #Aumenta sua pontuação se você passar dela
                    hud.clear() #Limpa o que ja estava escrito e atualiza com o debaixo
                    hud.write(f"Pontos: {score} \nCombustivel: {combustivel}%", align="center", font=("Arial", 18, "normal")) # Atualiza na tela a nova pontuação

            

            for inimigo in inimigos:
                inimigo.sety(inimigo.ycor() - inimigo.speed)    # Manda inimigos para baixo
                if inimigo.ycor() < -300:                        # Se passar desse ponto no plano
                    inimigo.goto(random.randint(-280, 280), random.randint(400, 800))   # Retorna aleatoriamente em uma dessas coordenadas indicadas
                    combustivel -= 1 # Perde combustivel se passar delas
                    hud.clear() #Limpa o que ja estava escrito 
                    hud.write(f"Pontos: {score} \nCombustivel: {combustivel}%", align="center", font=("Arial", 18, "normal")) # Atualiza na tela a nova pontuação


                if personagem.distance(inimigo) < 40: # Se caso o personagem colidir com inimigo
                    winsound.PlaySound("batida.wav", winsound.SND_ASYNC) # Som de batida
                    combustivel -= 25                                           # -25 de combustivel
                    time.sleep(0.1)                                                 #tempo para por 0.1 segundo
                    inimigo.goto(random.randint(-280, 280), random.randint(400, 800)) # Retorna para uma posicão aleatoria
                    hud.clear() #Limpa o que ja estava escrito 
                    hud.write(f"Pontos: {score} \nCombustivel: {combustivel}%", align="center", font=("Arial", 18, "normal")) # Atualiza na tela a nova pontuação
            


            for yoda in yodas:
                yoda.sety(yoda.ycor() - yoda.speed)                 # Manda o yoda para baixo
                if yoda.ycor() < -300:                                  # Se passar desse plano:
                    yoda.goto(random.randint(-280, 280), random.randint(400, 800))      # Repete aleatoriamente nessas coordenadas 
                
                if personagem.distance(yoda) < 40:                  # se ouver colisão do personagem com o yoda:
                    winsound.PlaySound("r2d2.wav", winsound.SND_ASYNC)  # Efeito sonoro do R2D2
                    score += 100                                         # Aumenta mais 100 a pontuação
                    if combustivel <= 100:                               # se o comubstivel tiver menor que 100
                        combustivel += 25                                # Aumenta combustivel em 25%
                        
                        hud.clear() #Limpa o que ja estava escrito 
                        hud.write(f"Pontos: {score} \nCombustivel: {combustivel}%", align="center", font=("Arial", 18, "normal")) # Atualiza na tela a nova pontuação
                        yoda.goto(random.randint(-280, 280), random.randint(400, 800)) # Manda o yoda para uma dessas coordenadas 
            if combustivel <= 0:        # Caso combustivel chegue a 0
                winsound.PlaySound("eusouseupai.wav", winsound.SND_ASYNC)  # Reproduz o som "I'am your Father" de Darth Vader 
                hud.clear()                 # Atualiza a tela
                hud.goto(0,0)               # Placar vai para as coordenadas x:0 e y:0 no Plano carteziano 
                hud.clear()                     # Apaga o placar que estava no topo 
                hud.write(f"  Game Over! \nPontuação: {score}", align="center", font=("Impact", 30, "normal")) # Mostra sua pontuação e Game Over
                #time.sleep(1)               # Progama Para                

                    

tela.onkeypress(start,'space')  # Inicia o jogo(chama a funçao start) quando tecla "espaço" for pressionada
tela.mainloop()                 # Janela nunca irá fechar
