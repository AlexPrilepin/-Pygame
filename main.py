import pygame
pygame.font.init()

fon = pygame.image.load('images/Fon.png')
fon.set_colorkey((255, 255, 255))
ns = pygame.image.load('images/ns.png')
ns.set_colorkey((255, 255, 255))
shes = pygame.image.load('images/shes.png')
shes.set_colorkey((255, 255, 255))
learn = pygame.image.load('images/learn.png')
learn.set_colorkey((255, 255, 255))
play_1 = pygame.image.load('images/play_1.png')
play_1.set_colorkey((255, 255, 255))
play_2 = pygame.image.load('images/play_2.png')
play_2.set_colorkey((255, 255, 255))
play_3 = pygame.image.load('images/play_3.png')
play_3.set_colorkey((255, 255, 255))
play_4 = pygame.image.load('images/play_4.png')
play_4.set_colorkey((255, 255, 255))
play_5 = pygame.image.load('images/play_5.png')
play_5.set_colorkey((255, 255, 255))
fon_shes = pygame.image.load('images/Fonshes.png')
fon_shes.set_colorkey((255, 255, 255))
sound_on = pygame.image.load('images/sound_on.png')
sound_on.set_colorkey((255, 255, 255))
sound_off = pygame.image.load('images/sound_off.png')
sound_off.set_colorkey((255, 255, 255))
menu = pygame.image.load('images/Menu.png')
menu.set_colorkey((255, 255, 255))
loading = pygame.image.load('images/Loading.png')
loading.set_colorkey((255, 255, 255))

level = 1
sound1 = False
open_1 = 0

pygame.init()
pygame.display.set_caption('Вступительное окно')
size = width, height = 1170, 650
screen = pygame.display.set_mode(size)
screen_shes = pygame.display.set_mode(size)
screen_loading = pygame.display.set_mode(size)

level = 1

x_pos, y_pos = 0, 0
main_win = True

clock = pygame.time.Clock()
t = 3

o_w = fon.get_rect(
    topleft=(0, 0))
screen.blit(fon, o_w)
o_w1 = shes.get_rect(
    topleft=(width - 120, 5))
o_w2 = ns.get_rect(
    topleft=(width // 2 - 180, 500))
o_w3 = learn.get_rect(
    topleft=(width // 2 - 520, 500))
o_w4 = play_1.get_rect(
    topleft=(width // 2 + 190, 500))

fs = fon_shes.get_rect(
    topleft=(0, 0))
screen.blit(fon_shes, fs)
o_w_menu = menu.get_rect(
    topleft=(width // 2 + 230, 500))

load = loading.get_rect(
    topleft=(0, 0))
screen.blit(loading, load)
f1 = open('info.txt').read().split('\n')
lvl = int(f1[0])
running = True
reload = 0
c = 0
b = 0
draw = 0
while running:
    if b > 0:
        b += 1
    if b == 15:
        f1 = open('info.txt').read().split('\n')
        lvl = int(f1[0])
        sasound = int(f1[1])
        w = open("info.txt", 'w')
        w.write(str(lvl) + '\n')
        if sound1 == 0:
            w.write(str(0) + '\n')
        else:
            w.write(str(1) + '\n')
        w.close()
        if lvl == 1:
            import pygraph
        elif lvl == 2:
            import pygraph_2
        elif lvl == 3:
            import pygraph_3
        elif lvl == 4:
            import pygraph_4
        elif lvl == 5:
            import pygraph_5  
    if c > 0:
        c += 1
    if c == 15:
        f1 = open('info.txt').read().split('\n')
        lvl = int(f1[0])
        w = open("info.txt", 'w')
        w.write(str(lvl) + '\n')
        if sound1 == 0:
            w.write(str(0) + '\n')
        else:
            w.write(str(1) + '\n')
        w.close()
        import pygraph
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
        if lvl == 1:
            o_w4 = play_1.get_rect(
                topleft=(width // 2 + 190, 500))
            screen.blit(play_1, o_w4)
        elif lvl == 2:
            o_w4 = play_2.get_rect(
                topleft=(width // 2 + 190, 500))
            screen.blit(play_2, o_w4)
        elif lvl == 3:
            o_w4 = play_3.get_rect(
                topleft=(width // 2 + 190, 500))
            screen.blit(play_3, o_w4)
        elif lvl == 4:
            o_w4 = play_4.get_rect(
                topleft=(width // 2 + 190, 500))
            screen.blit(play_4, o_w4)
        elif lvl == 5:
            o_w4 = play_5.get_rect(
                topleft=(width // 2 + 190, 500))
            screen.blit(play_5, o_w4)
        if draw > 0:
            draw -= 1
            pygame.draw.rect(screen, (255, 255, 255), (370, 200, 400, 100))
            pygame.draw.rect(screen, (255, 0, 0), (360, 190, 420, 120), 10)
            fsс = pygame.font.SysFont('serif', 48)
            complexity = fsс.render("В разработке...", True, (255, 0, 0))
            screen_shes.blit(complexity, (410, 220))
        if event.type == pygame.MOUSEBUTTONUP:
            x_pos, y_pos = event.pos
            if x_pos in list(range(width - 120, width + 100)) and y_pos in list(range(5, 105)):
                open_1 = 1
            if x_pos in list(range(width // 2 - 180, width // 2 + 140)) and y_pos in list(range(400, 600)):
                print('2')
                open_1 = 2
                c += 1
            if x_pos in list(range(width // 2 - 520, width // 2 - 200)) and y_pos in list(range(400, 600)):
                print('3')
                draw = 45
                import training2
            if x_pos in list(range(width // 2 + 190, width // 2 + 520)) and y_pos in list(range(400, 600)):
                print('4')
                open_1 = 2
                b += 1

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
        o_w_menu = menu.get_rect(
            topleft=(width // 2 + 230, 500))
        screen.blit(menu, o_w_menu)

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
            elif x_pos in list(range(width // 2 + 230, width // 2 + 570)) and y_pos in list(range(500, 600)):
                print('Меню')
                open_1 = 0
                reload = 10

        if level == 1:
            pygame.draw.circle(screen, (255, 255, 255), (390, 85), 48, 10)
        elif level == 2:
            pygame.draw.circle(screen, (255, 255, 255), (628, 82), 47, 10)
        elif level == 3:
            pygame.draw.circle(screen, (255, 255, 255), (856, 83), 47, 10)

    elif open_1 == 2:
        load = loading.get_rect(
            topleft=(0, 0))
        screen.fill('white')
        screen.blit(loading, load)
        fsс = pygame.font.SysFont('serif', 48)
        loading_txt = fsс.render("Loading...", True, (255, 0, 0))
        screen_loading.blit(loading_txt, (500, 550))
        clock.tick(t)
    pygame.display.flip()
pygame.quit()
