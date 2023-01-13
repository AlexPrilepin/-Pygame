import pygame
pygame.font.init()

fon_f = pygame.image.load('Fon_finish.png')
fon_f.set_colorkey((255, 255, 255))

pygame.init()
pygame.display.set_caption('Окно финиша')
size = width, height = 1170, 650
screen = pygame.display.set_mode(size)
x_pos, y_pos = 0, 0

o_w_f = fon_f.get_rect(
    topleft=(0, 0))
screen.blit(fon_f, o_w_f)

running = True

while running:
    x_pos, y_pos = -1, -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    o_w = fon_f.get_rect(
        topleft=(0, 0))
    screen.fill('white')
    screen.blit(fon_f, o_w_f)

    if event.type == pygame.MOUSEBUTTONUP:
        x_pos, y_pos = event.pos
        if x_pos in list(range(width // 2 + 160, width // 2 + 530)) and y_pos in list(range(470, 640)):
            print('Menu')
            running = False
    pygame.display.flip()

import main
