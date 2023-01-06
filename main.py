import pygame
pygame.font.init()

fon = pygame.image.load('Fon.png')
fon.set_colorkey((255, 255, 255))
ns = pygame.image.load('ns.png')
ns.set_colorkey((255, 255, 255))
shes = pygame.image.load('shes.png')
shes.set_colorkey((255, 255, 255))
learn = pygame.image.load('learn.png')
learn.set_colorkey((255, 255, 255))
play_a_l = pygame.image.load('play_a_l.png')
play_a_l.set_colorkey((255, 255, 255))
sound_on = pygame.image.load('sound_on.png')
sound_on.set_colorkey((255, 255, 255))
sound_off = pygame.image.load('sound_off.png')
sound_off.set_colorkey((255, 255, 255))
fon_shes = pygame.image.load('Fonshes.png')
fon_shes.set_colorkey((255, 255, 255))
level = 1
sound1 = False
open_1 = 0

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Вступительное окно')
    size = width, height = 1170, 650
    screen = pygame.display.set_mode(size)
    screen_shes = pygame.display.set_mode(size)
    level = 1
    x_pos, y_pos = 0, 0
    main_win = True
    o_w = fon.get_rect(
        topleft=(0, 0))
    screen.blit(fon, o_w)
    o_w1 = shes.get_rect(
        topleft=(width - 120, 5))
    o_w2 = ns.get_rect(
        topleft=(width // 2 - 180, 500))
    o_w3 = learn.get_rect(
        topleft=(width // 2 - 520, 500))
    o_w4 = play_a_l.get_rect(
        topleft=(width // 2 + 190, 500))

    fs = fon_shes.get_rect(
        topleft=(0, 0))
    screen.blit(fon_shes, fs)

    running = True
    reload = 0
    while running:
        x_pos, y_pos = -1, -1
        if reload > 0:
            reload -= 1
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
                topleft=(width // 2 - 180, 500))
            screen.blit(ns, o_w2)
            o_w3 = learn.get_rect(
                topleft=(width // 2 - 520, 500))
            screen.blit(learn, o_w3)
            o_w4 = play_a_l.get_rect(
                topleft=(width // 2 + 190, 500))
            screen.blit(play_a_l, o_w4)

            if event.type == pygame.MOUSEBUTTONUP:
                x_pos, y_pos = event.pos
                if x_pos in list(range(width - 120, width + 100)) and y_pos in list(range(5, 105)):
                    open_1 = 1
                if x_pos in list(range(width // 2 - 180, width // 2 + 140)) and y_pos in list(range(400, 600)):
                    print('2')
                if x_pos in list(range(width // 2 - 520, width // 2 - 200)) and y_pos in list(range(400, 600)):
                    print('3')
                if x_pos in list(range(width // 2 + 190, width // 2 + 520)) and y_pos in list(range(400, 600)):
                    print('4')
        elif open_1 == 1:
            x_pos, y_pos = -1, -1
            fs = fon_shes.get_rect(
                topleft=(0, 0))
            screen_shes.fill('white')
            screen_shes.blit(fon_shes, fs)
            fsс = pygame.font.SysFont('serif', 48)
            complexity = fsс.render("Сложность:", True, (0, 0, 0))
            screen_shes.blit(complexity, (10, 50))
            fsa = pygame.font.SysFont('serif', 48)
            achievement = fsa.render("Достижения:", True, (0, 0, 0))
            screen_shes.blit(achievement, (10, 200))
            fss = pygame.font.SysFont('serif', 48)
            sound = fss.render("Звук:", True, (0, 0, 0))
            screen_shes.blit(sound, (275, 500))
            pygame.draw.rect(screen, (200, 253, 203), (width // 2 - 200, 400, 1000, 1000))
            if sound1 is True:
                fs = sound_on.get_rect(
                    topleft=(width // 2 - 50, 450))
                screen_shes.blit(sound_on, fs)
            else:
                fs = sound_off.get_rect(
                    topleft=(width // 2 - 50, 450))
                screen_shes.blit(sound_off, fs)
            if event.type == pygame.MOUSEBUTTONUP and reload == 0:
                x_pos, y_pos = event.pos
                if x_pos in list(range(width // 2 - 250, width // 2 - 160)) and y_pos in list(range(15, 110)):
                    print('Сложность1')
                    level = 1
                    reload = 10
                elif x_pos in list(range(width // 2 - 10, width // 2 + 100)) and y_pos in list(range(15, 110)):
                    print('Сложность2')
                    level = 2
                    reload = 10
                elif x_pos in list(range(width // 2 + 230, width // 2 + 320)) and y_pos in list(range(15, 110)):
                    print('Сложность3')
                    level = 3
                    reload = 10
                elif x_pos in list(range(width // 2 - 280, width // 2 - 50)) and y_pos in list(range(180, 380)):
                    print('Достижения')
                    reload = 10
                elif x_pos in list(range(width // 2 - 50, width // 2 + 170)) and y_pos in list(range(450, 600)):
                    sound1 = not sound1
                    reload = 10
            if level == 1:
                pygame.draw.circle(screen, (255, 255, 255), (390, 85), 48, 10)
            elif level == 2:
                pygame.draw.circle(screen, (255, 255, 255), (628, 82), 47, 10)
            elif level == 3:
                pygame.draw.circle(screen, (255, 255, 255), (856, 83), 47, 10)
        pygame.display.flip()
    pygame.quit()
