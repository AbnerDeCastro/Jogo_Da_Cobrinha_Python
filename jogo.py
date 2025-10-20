import pygame
from pygame.locals import *
import random
import time

#Criando a tela do jogo
WINDOWS_WITDH = 600
WINDOWS_HEIGTH = 600
POS_INICIAL_X = WINDOWS_WITDH/2
POS_INICIAL_Y = WINDOWS_HEIGTH/2
BLOCK = 10
pontos = 0
velocidade =10

pygame.font.init()
pygame.display.set_caption('Jogo da Cobrinha')
fonte = pygame.font.SysFont('arial', 35, True, True) #negrito é italico

#Cirando a funcão de game ouver quando bater nas bordas

def colisao(pos1, pos2):
    return pos1 == pos2

def verifica_margens(pos):
    if 0 <= pos [0] < WINDOWS_WITDH and 0 <= pos [1] < WINDOWS_HEIGTH:
        return False
    else:
        return True
    
def gera_pos_aleatoria():
    x = random.randint(0, WINDOWS_WITDH)
    y = random.randint(0, WINDOWS_HEIGTH)

    if (x,y) in obistaculo_pos:
        gera_pos_aleatoria()

    if (x,y) in obistaculo_pos:
        gera_pos_aleatoria

    return x // BLOCK * BLOCK ,y // BLOCK * BLOCK

def game_over():
    fonte = pygame.font.SysFont('arial', 60, True, True)
    gameover = 'GAME OVER'
    text_ouver = fonte.render(gameover, True, (255,255,255))
    window.blit(text_ouver,(110, 300))
    pygame.display.update()
    time.sleep(5)
    pygame.quit()
    quit()
    

pygame.init()
window = pygame.display.set_mode((WINDOWS_WITDH, WINDOWS_HEIGTH))

cobra_pos = [(POS_INICIAL_X,POS_INICIAL_Y), (POS_INICIAL_X + BLOCK, POS_INICIAL_Y),(POS_INICIAL_X + 2* BLOCK, POS_INICIAL_Y)]
cobra_surface = pygame.Surface((BLOCK, BLOCK))
cobra_surface.fill((53,59,72))
direcao = K_LEFT

obistaculo_pos = []
obistaculo_surface = pygame.Surface((BLOCK, BLOCK))
obistaculo_surface.fill((0,0,0))

maca_surface = pygame.Surface([BLOCK,BLOCK])
maca_surface.fill((255,0,0))
maca_pos = gera_pos_aleatoria()

while True:
    pygame.time.Clock().tick(velocidade)
    window.fill((68,189,50))

    mensagem = f'Pontos : {pontos}'
    texto = fonte.render(mensagem, True,(255,255,255))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            quit()
            
    #Introduzindo os movimentos do teclados para mover a cobra
        elif evento.type == KEYDOWN:
            if evento.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                if evento.key == K_UP and direcao == K_DOWN:
                    continue
                elif evento.key == K_DOWN and direcao == K_UP:
                    continue
                elif evento.key == K_LEFT and direcao == K_RIGHT:
                    continue
                elif evento.key == K_RIGHT and direcao == K_LEFT:
                    continue
                else:
                    direcao = evento.key

    window.blit(maca_surface,maca_pos)

    if (colisao(cobra_pos[0], maca_pos)):
        cobra_pos.append((-10, -10))
        maca_pos = gera_pos_aleatoria()
        obistaculo_pos.append(gera_pos_aleatoria())
        pontos +=1
        if pontos %5 == 0: #% retorna o resto da divisão
            velocidade += 2

    for pos in obistaculo_pos:
        if colisao(cobra_pos[0], pos):
            game_over()
        window.blit(obistaculo_surface, pos)
               
    for pos in cobra_pos:
        window.blit(cobra_surface,pos)

    for item in range (len(cobra_pos)-1,0,-1):
        if colisao (cobra_pos[0],cobra_pos[item]):
            game_over
        cobra_pos[item] = cobra_pos[item -1]   

    if verifica_margens(cobra_pos[0]):
        game_over()
    
    if direcao == K_RIGHT:
        cobra_pos[0] = cobra_pos[0][0] + BLOCK, cobra_pos[0][1] # Movimenta a cobra para a direita
    elif direcao == K_LEFT:
        cobra_pos[0] = cobra_pos[0][0] - BLOCK, cobra_pos[0][1] # Movimenta a cobra para a esquerda
    elif direcao == K_UP:    
        cobra_pos[0] = cobra_pos[0][0], cobra_pos[0][1] - BLOCK # Movimenta a cobra para cima
    elif direcao == K_DOWN:    
        cobra_pos[0] = cobra_pos[0][0], cobra_pos[0][1] + BLOCK  # Movimenta a cobra para baixo

    window.blit(texto,(420,30))       

    pygame.display.update()