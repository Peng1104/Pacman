import pygame
from os import path

from settings import IMG_DIR, FPS, PLAYING, QUIT

# Criando a função que inicia a tela de Game Over
def final_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'gameover.png')).convert()
    background_rect = background.get_rect()

    while True:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                return QUIT

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    return PLAYING

        # A cada loop, redesenha o fundo 
        window.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state