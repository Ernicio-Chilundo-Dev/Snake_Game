import pygame
import time
import random

# Inicializacao do pygame
pygame.init

# Dimensoes de tela
largura = 800
altura = 600

# Cores 
preto = (0,0,0)
branco = (255,255,255)
vermelho = (213,50,80)
verde = (0,255,0)
azul = (50,153,213)

# Configuracao da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobra")

# Relogio
relogio = pygame.time.clock()

# Tamanho dos blocos da cobra
tamanho_bloco = 10
velocidade = 15

# Fonte
fonte_estilo = pygame.font.SysFont("bahnschrift",25)
fonte_potuancao = pygame.font.SysFont("comicsansms", 35)

def sua_potuancao(pontos):
    valor = fonte_potuancao.render(f"Sua potuancao: {pontos}", True, azul)
    tela.blit(valor,[10,10])
    
    
def cobra(tamanho_bloco, lista_cobra):
    for bloco in lista_cobra:
        pygame.draw.rect(tela, verde[bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])
        
        
def mensagem(msg, cor):
    mensagem = fonte_estilo.render(msg, True, cor)
    tela.blit(mensagem, [largura/6, altura/3])
    
def jogo():
    game_over = False
    game_close = False
    
    
# Posocao inicial da cobra
x1 = largura /2
y1 = altura / 2

# Corpo da cobra
lisa_cobra = []
comprimento_cobra =1

# posicao da comida

comida_x = round(random.randrange(0, largura - tamanho_bloco) / 10.0)
comida_y = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0


