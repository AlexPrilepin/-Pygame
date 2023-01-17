import pygame
from random import choice, randint

hp_boost_pic = pygame.image.load('images/upgrade_hp.png')
speed_boost_pic = pygame.image.load('images/speed_boost.png')
damage_boost_pic = pygame.image.load('images/upgrade_damage.png')
portal = pygame.image.load('images/portal_for_menu.png')
coin = pygame.image.load('images/coin.png')
coin.set_colorkey((255, 255, 255))
small_coin = pygame.image.load('images/small_coin.png')
coin.set_colorkey((255, 255, 255))


pygame.init()
pygame.display.set_caption('Soul Knight: PC Edition')
size = width, height = 1200, 900
screen = pygame.display.set_mode(size)
running = True
v = 100
chosen = None
clock = pygame.time.Clock()
fps = 60
f = open('earning.txt').read().split('\n')
hero_hp = int(f[0])
hero_2_hp = int(f[1])
hero_coins = int(f[2])
f1 = open('buffs.txt').read().split('\n')
hp_boost = int(f1[0])
damage_boost = int(f1[1])
speed_boost = int(f1[2])
angle = 0
writing_cd = 0
writing_type = 1
while running:
    screen.fill((247, 247, 247))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            s_x, s_y = event.pos
            if s_y in range(600, 700):
                if s_x in list(range(250, 350)):
                    chosen = 1
                elif s_x in list(range(550, 650)):
                    chosen = 2
                elif s_x in list(range(850, 950)):
                    chosen = 3
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] == True:
            if chosen == 1:
                writing_cd = 20
                if hero_coins >= 25:
                    hero_coins -= 25
                    hp_boost += 2
                    hero_hp += 2
                    hero_2_hp += 2
                    writing_type = 1
                    chosen = None
                else:
                    writing_type = 2
##                    
            elif chosen == 2:
                writing_cd = 20
                if hero_coins >= 20:
                    hero_coins -= 20
                    damage_boost += 1
                    writing_type = 1
                    chosen = None
                else:
                    writing_type = 2
##                    
            elif chosen == 3:
                writing_cd = 20
                if hero_coins >= 30:
                    hero_coins -= 30
                    speed_boost += 1
                    chosen = None
                    writing_type = 1
                else:
                    writing_type = 2
                    
##                    
        if keys[pygame.K_y] == True:
            running = False
    
    g_l_r = portal.get_rect(
        topleft=(0, -100))
    rot_image = pygame.transform.rotate(portal, angle)
    angle += 15
    if angle == 360:
        angle = 0
    rot_rect = rot_image.get_rect(center=g_l_r.center)
    rot_image.set_colorkey((0, 123, 0))
    screen.blit(rot_image, rot_rect)
                    
    g_l_r1 = hp_boost_pic.get_rect(
            topleft=(250, 600))
    screen.blit(hp_boost_pic, g_l_r1)
    g_l_r1 = speed_boost_pic.get_rect(
            topleft=(850, 600))
    screen.blit(speed_boost_pic, g_l_r1)
    g_l_r1 = damage_boost_pic.get_rect(
            topleft=(550, 600))
    screen.blit(damage_boost_pic, g_l_r1)
    g_l_r1 = coin.get_rect(
            topleft=(1120, 780))
    screen.blit(coin, g_l_r1)
    n = pygame.font.Font(None, 100)
    t = n.render(str(hero_coins), True, (255, 200, 0))
    screen.blit(t, (1030, 780))

    pygame.draw.rect(screen, (255, 255, 255), (200, 25, 800, 125))
    pygame.draw.rect(screen, (0, 0, 255), (200, 25, 800, 125), 10)
    n = pygame.font.Font(None, 40)
    t = n.render('После покупки всех нужных усилений,', True, (0, 0, 0))
    screen.blit(t, (330, 45))
    t = n.render('нажмите "Y", чтобы перейти на следующий уровень', True, (0, 0, 0))
    screen.blit(t, (240, 85))
    
    if chosen != None:
        pygame.draw.rect(screen, (255, 0, 0), (250 + 300 * (chosen - 1) - 10, 590, 120, 120), 10)
    pygame.draw.rect(screen, (255, 255, 255), (200, 750, 800, 125))
    pygame.draw.rect(screen, (0, 0, 255), (200, 750, 800, 125), 10)
    if chosen == None:
        n = pygame.font.Font(None, 32)
        t = n.render('Нажмите на усиление, чтобы увидеть дополнительную информацию.', True, (0, 0, 0))
        screen.blit(t, (220, 800))
    elif chosen == 2:
        n = pygame.font.Font(None, 30)
        t = n.render('Увеличение урона от оружия на 1 единицу. Не влияет на способности.', True, (0, 0, 0))
        screen.blit(t, (260, 770))
        t = n.render('Стоимость усиления: 20 ', True, (0, 0, 0))
        g_l_r1 = small_coin.get_rect(
                topleft=(690, 795))
        screen.blit(small_coin, g_l_r1)
        screen.blit(t, (450, 800))
        t = n.render('Нажмите "Enter" для совершения покупки.', True, (0, 0, 0))
        screen.blit(t, (380, 830))
    elif chosen == 1:
        n = pygame.font.Font(None, 30)
        t = n.render('Увеличение запаса здоровья обоих персонажей на 2 единицы.', True, (0, 0, 0))
        screen.blit(t, (260, 770))
        t = n.render('Стоимость усиления: 25 ', True, (0, 0, 0))
        screen.blit(t, (450, 800))
        t = n.render('Нажмите "Enter" для совершения покупки.', True, (0, 0, 0))
        screen.blit(t, (380, 830))
        g_l_r1 = small_coin.get_rect(
                topleft=(690, 795))
        screen.blit(small_coin, g_l_r1)
    elif chosen == 3:
        n = pygame.font.Font(None, 30)
        t = n.render('Увеличение скорочти обоих персонажей на 15%.', True, (0, 0, 0))
        screen.blit(t, (330, 770))
        t = n.render('Стоимость усиления: 30 ', True, (0, 0, 0))
        screen.blit(t, (450, 800))
        t = n.render('Нажмите "Enter" для совершения покупки.', True, (0, 0, 0))
        screen.blit(t, (380, 830))
        g_l_r1 = small_coin.get_rect(
                topleft=(690, 795))
        screen.blit(small_coin, g_l_r1)

    if writing_cd:
        pygame.draw.rect(screen, (255, 255, 255), (400, 350, 400, 100))
        pygame.draw.rect(screen, (255 * ((writing_type - 1) % 2), 0, 255 * ((writing_type) % 2)), (400, 350, 400, 100), 10)
        writing_cd -= 1
        if writing_type == 1:
            n = pygame.font.Font(None, 90)
            t = n.render('Успешно!', True, (0, 0, 0))
            screen.blit(t, (450, 370))
        else:
            n = pygame.font.Font(None, 50)
            t = n.render('Недостаточно монет!', True, (0, 0, 0))
            screen.blit(t, (420, 380))

    clock.tick(fps)
    pygame.display.flip()

    
try:
    with open("earning.txt", 'w'):
        pass
except IOError:
    pass
w = open("earning.txt", 'w')
w.write(str(hero_hp) + '\n')
w.write(str(hero_2_hp) + '\n')
w.write(str(hero_coins) + '\n')
w.close()

try:
    with open("buffs.txt", 'w'):
        pass
except IOError:
    pass
w = open("buffs.txt", 'w')
w.write(str(hp_boost) + '\n')
w.write(str(damage_boost) + '\n')
w.write(str(speed_boost) + '\n')
w.close()

import pygraph_3
