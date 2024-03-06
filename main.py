import pygame
from pygame import Surface, Rect

window_widit = 1900
window_heigth = 1000

# Inicializar o módulo pygame
pygame.init()

print('Setup start')

# Criação de janela no pygame
window: Surface = pygame.display.set_mode(size=(window_widit, window_heigth))

# carregar imagem e gerar uma superfície
bg_surf: Surface = pygame.image.load('./asset/bg.png').convert_alpha()
player1_surf: Surface = pygame.image.load('./asset/player1.png').convert_alpha()

# Carregar som e deixar tocando
pygame.mixer_music.load('./asset/fase1.mp3')
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.3)


# Obter retângulo da superfície
bg_react: Rect = bg_surf.get_rect(left=0, top=0)
player1_react: Rect = player1_surf.get_rect(left=0, top=230)


# Desenhar na window
window.blit(source=bg_surf, dest=bg_react)
window.blit(source=player1_surf, dest=player1_react)

# att janela
pygame.display.flip()

print('Setup end')

# Colocar relogio no jogo
clock = pygame.time.Clock()

print('loop start')
while True:
    clock.tick(180)
    # print(f'{clock.get_fps() :.0f}') # executar print
    window.blit(source=bg_surf, dest=bg_react)
    window.blit(source=player1_surf, dest=player1_react)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Setup end')
            pygame: quit()
            quit()

    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        player1_react.centery -= 1
    if pressed_key[pygame.K_s]:
        player1_react.centery += 1
    if pressed_key[pygame.K_d]:
        player1_react.centerx += 1
    if pressed_key[pygame.K_a]:
        player1_react.centerx -= 1

        pass


