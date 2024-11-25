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
        pygame.draw.rect(tela, verde[bloco[0]], bloco[1], tamanho_bloco, tamanho_bloco)
        