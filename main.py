import pygame

fon = pygame.image.load('Fon.png')
fon.set_colorkey((255, 255, 255))
ns = pygame.image.load('ns.png')
ns.set_colorkey((255, 255, 255))
shes = pygame.image.load('shes.png')
shes.set_colorkey((255, 255, 255))

fon_shes = pygame.image.load('Fonshes.png')
fon_shes.set_colorkey((255, 255, 255))

open_1 = 0

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Вступительное окно')
    size = width, height = 1170, 650
    screen = pygame.display.set_mode(size)
    screen_shes = pygame.display.set_mode(size)

    x_pos, y_pos = 0, 0
    main_win = True
    o_w = fon.get_rect(
        topleft=(0, 0))
    screen.blit(fon, o_w)
    o_w1 = shes.get_rect(
        topleft=(width - 120, 5))
    o_w2 = ns.get_rect(
        topleft=(width // 2 - 145, 500))

    fs = fon_shes.get_rect(
        topleft=(0, 0))
    screen.blit(fon_shes, fs)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if open_1 == 0:
            o_w = fon.get_rect(
                topleft=(0, 0))
            screen.fill('white')
            screen.blit(fon, o_w)
            o_w1 = shes.get_rect(
                topleft=(width - 120, 5))
            screen.blit(shes, o_w1)
            o_w2 = ns.get_rect(
                topleft=(width // 2 - 145, 500))
            screen.blit(ns, o_w2)

            if event.type == pygame.MOUSEBUTTONUP:
                x_pos, y_pos = event.pos
                if x_pos in list(range(width - 120, width + 100)) and y_pos in list(range(5, 105)):
                    open_1 = 1
                if x_pos in list(range(width // 2 - 145, width // 2 + 225)) and y_pos in list(range(400, 600)):
                    open_1 = 2
        elif open_1 == 1:
            fs = fon_shes.get_rect(
                topleft=(0, 0))
            screen_shes.fill('white')
            screen_shes.blit(fon_shes, fs)
        elif open_1 == 2:

        pygame.display.flip()
    pygame.quit()