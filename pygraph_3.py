import pygame
from random import choice, randint
from math import sqrt, asin, pi, sin, cos


goblin_l = pygame.image.load('npc_3_l.png')
goblin_l.set_colorkey((255, 255, 255))
goblin_r = pygame.image.load('npc_3_r.png')
goblin_r.set_colorkey((255, 255, 255))
hero_l = pygame.image.load('not_bandit.png')
hero_l.set_colorkey((255, 255, 255))
hero_r = pygame.image.load('bandit.png')
hero_r.set_colorkey((255, 255, 255))
other_hero_l = pygame.image.load('other_hero_l.png')
other_hero_l.set_colorkey((255, 255, 255))
other_hero_r = pygame.image.load('other_hero_r.png')
other_hero_r.set_colorkey((255, 255, 255))
pol = pygame.image.load('pol_3.png')
pol.set_colorkey((255, 255, 255))
wall_hor = pygame.image.load('wall_hor_3.png')
wall_hor.set_colorkey((255, 255, 255))
wall_ver = pygame.image.load('wall_ver_3.png')
wall_ver.set_colorkey((255, 255, 255))
rifle_l = pygame.image.load('rifle_l.png')
rifle_l.set_colorkey((24, 29, 35))
rifle_r = pygame.image.load('rifle_r.png')
rifle_r.set_colorkey((24, 29, 35))
bullet = pygame.image.load('bullet.png')
bullet.set_colorkey((255, 255, 255))
npc_bullet_l = pygame.image.load('flame_of_dragon_l.png')
npc_bullet_l.set_colorkey((255, 255, 255))
npc_bullet_r = pygame.image.load('flame_of_dragon_r.png')
npc_bullet_r.set_colorkey((255, 255, 255))
courpse = pygame.image.load('courpse_1.png')
courpse.set_colorkey((255, 255, 255))
hp_bar = pygame.image.load('health_points.png')
hp_bar.set_colorkey((255, 255, 255))
hc = pygame.image.load('hero_dead.png')
hc.set_colorkey((255, 255, 255))
walkthrough = pygame.image.load('walkthrough.png')
walkthrough.set_colorkey((255, 255, 255))
trade = pygame.image.load('trading.png')
trade.set_colorkey((255, 255, 255))
portal = pygame.image.load('portal.png')
portal.set_colorkey((255, 255, 255))
coin = pygame.image.load('coin.png')
coin.set_colorkey((255, 255, 255))


aim = True
GG_1, GG_2 = False, False
courpses = []
room = 1

class Nepice:
    def __init__(self, x, y):
        self.nx = choice([-1, 1])
        self.ny = choice([-1, 1])
        self.y = y
        self.x = x
        self.hp = 8
        self.damage = 2
        self.cd = 6

    def get_damage(self, amount):
        global courpses, coins
        self.hp -= amount
        if self.hp <= 0:
            courpses.append((self.x, self.y))
        
            
    
    def move(self, hp, stop):
        if (sqrt((hero_2.x - self.x) ** 2 + (hero_2.y - self.y) ** 2) <= sqrt((hero.x - self.x) ** 2 + (hero.y - self.y) ** 2) and hero_2.hp > 0) or hero.hp <= 0:
            aim_x, aim_y = hero_2.x, hero_2.y
        else:
            aim_x, aim_y = hero.x, hero.y
        if aim_x > self.x:
            self.nx = 1
        else:
            self.nx = -1
        if aim_y > self.y:
            self.ny = 1
        else:
            self.ny = -1
        if not stop:
            self.x += self.nx * v / fps
            self.y += self.ny * v / fps
            if self.x <= 30:
                self.nx *= -1
            if self.y <= 50:
                self.ny *= -1
            if self.x > 1200 - 100:
                self.nx *= -1
            if self.y > 800 - 120:
                self.ny *= -1
        self.draw(hp)
        
    def draw(self):
        pass

    def attack(self):
        if (sqrt((hero_2.x - self.x) ** 2 + (hero_2.y - self.y) ** 2) <= sqrt((hero.x - self.x) ** 2 + (hero.y - self.y) ** 2) and hero_2.hp > 0) or hero.hp <= 0:
            aim_x, aim_y = hero_2.x, hero_2.y
        else:
            aim_x, aim_y = hero.x, hero.y
        bullets.append(NPC_bullet(self.x, self.y, aim_x, aim_y))
        



class Goblin(Nepice):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.hp = 8
        
    def draw(self, hp):
        if self.nx == -1:
            g_l_r = goblin_l.get_rect(
                topleft=(self.x, self.y))
            screen.blit(goblin_l, g_l_r)
        else:
            g_l_r = goblin_r.get_rect(
                topleft=(self.x, self.y))
            screen.blit(goblin_r, g_l_r)
        pygame.draw.rect(screen, (0, 0, 0), (self.x - 2, self.y - 12, 72, 12), 4)
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y - 10, int(70 * hp / 8), 10))
        
            
npc = []
bullets = []
npc_bullets = []



class NPC_bullet:
    def __init__(self, start_x, start_y, end_x, end_y):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x + randint(-200, 200)
        self.end_y = end_y + randint(-200, 200)
        self.damage = 2
        self.x, self.y = self.start_x, self.start_y
        self.count_move = 200
        self.angle = int(asin((self.start_y - self.end_y) / sqrt((self.end_x - self.start_x) ** 2 + (self.end_y - self.start_y) ** 2)) / pi * 180)

    def draw(self):
        if self.start_x < self.end_x:
            self.x += 16 * abs(cos(self.angle * pi / 180))
        else:
            self.x -= 16 * abs(cos(self.angle * pi / 180))
        if self.start_y < self.end_y:
            self.y += 16 * abs(sin(self.angle * pi / 180))
        else:
            self.y -= 16 * abs(sin(self.angle * pi / 180))
        self.count_move -= 15

        
        if self.x < 30 or self.x > 1112 or self.y < 30 or self.y > 680:
            pygame.draw.circle(screen, (0, 0, 255), (self.x + 30, self.y + 55), 15)
            return True
        if int(self.x + 30) in list(range(int(hero_2.x), int(hero_2.x + 90))) and int(self.y + 50) in list(range(int(hero_2.y), int(hero_2.y + 70))) and not GG_2:
            hero_2.get_damage(self.damage)
            return True
        elif int(self.x + 30) in list(range(int(hero.x), int(hero.x + 90))) and int(self.y + 50) in list(range(int(hero.y), int(hero.y + 70))) and not GG_1:
            hero.get_damage(self.damage)
            return True
        if self.count_move <= 0:
            return True
        g_l_r = npc_bullet_r.get_rect(
            topleft=(self.x, self.y))
        if self.start_x < self.end_x:
            rot_image = pygame.transform.rotate(npc_bullet_r, self.angle)
        else:
            rot_image = pygame.transform.rotate(npc_bullet_l, -self.angle)
        rot_rect = rot_image.get_rect(center=g_l_r.center)
        rot_image.set_colorkey((255, 255, 255))
        screen.blit(rot_image, rot_rect)
        return False



class Hero_bullet:
    def __init__(self, start_x, start_y, end_x, end_y, damage=4, super_bullet=False):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.damage = damage
        self.x, self.y = self.start_x, self.start_y
        self.super_bullet = super_bullet
        try:
            self.angle = int(asin((self.start_y - self.end_y) / sqrt((self.end_x - self.start_x) ** 2 + (self.end_y - self.start_y) ** 2)) / pi * 180)
        except ZeroDivisionError:
            self.angle = int(asin((self.start_y - self.end_y) / 0.00000000000000001) / pi * 180)

    def draw(self):
        n = 16
        if self.super_bullet:
            n *= 2
        if self.start_x < self.end_x:
            self.x += n * abs(cos(self.angle * pi / 180))
        else:
            self.x -= n * abs(cos(self.angle * pi / 180))
        if self.start_y < self.end_y:
            self.y += n * abs(sin(self.angle * pi / 180))
        else:
            self.y -= n * abs(sin(self.angle * pi / 180))
        if self.x < 30 or self.x > 1112 or self.y < 30 or self.y > 680:
            pygame.draw.circle(screen, (255, 0, 0), (self.x + 30, self.y + 55), 15)
            return True
        for num, i in enumerate(npc):
            if int(self.x + 30) in list(range(int(i.x), int(i.x + 70))) and int(self.y + 50) in list(range(int(i.y), int(i.y + 50))):
                i.get_damage(self.damage)
                pygame.draw.circle(screen, (255, 0, 0), (self.x + 30, self.y + 55), 15)
                return True
        if not self.super_bullet:
            g_l_r = bullet.get_rect(
                topleft=(self.x + 35, self.y + 50))
            screen.blit(bullet, g_l_r)
        else:
            hm = pygame.image.load('super_bullet.png')
            hm.set_colorkey((255, 255, 255))
            g_l_r = hm.get_rect(
                topleft=(self.x + 35, self.y + 50))
            screen.blit(hm, g_l_r)
        return False
                    

class Hero:
    def __init__(self, typer):
        self.x = typer * 350
        self.y = 600
        self.nx = 1
        self.tp = typer
        self.weapons = [[rifle_r, rifle_l]]
        self.curr_weapon = self.weapons[0]
        self.target_x = 1000
        self.target_y = 600
        self.angle = 0
        self.hp = 10
        self.total = 10
        self.cd = 0
        if typer == 1:
            self.typer_r = hero_r
            self.typer_l = hero_l
        else:
            self.typer_r = other_hero_r
            self.typer_l = other_hero_l
        self.draw()
            

    def get_damage(self, num):
        global GG_1, GG_2
        self.hp -= num
        if self.hp <= 0:
            if self.tp == 1:
                GG_1 = True
            else:
                GG_2 = True

    def move(self, m_x, m_y):
        if ((GG_1 == True and self.tp == 1) or (GG_2 == True and self.tp == 2)):
            return
        if self.x + m_x <= 10:
            return
        if self.y + m_y <= 40:
            return
        if self.x + m_x > 1100:
            return
        if self.y + m_y > 800 - 125:
            return
        if room == 1 and self.x + m_x in list(range(0, 150)) and self.y + m_y in list(range(0, 200)):
            return
        self.x += m_x
        self.y += m_y
        if m_x < 0:
            self.nx = -1
        elif m_x > 0:
            self.nx = 1

    def target(self, x, y):
        self.target_x = x
        self.target_y = y
    
    def shoot(self, s_x=0, s_y=0):
        global bullets
        if self.cd == 0  and not ((GG_1 == True and self.tp == 1) or (GG_2 == True and self.tp == 2)):
            if aim or self.tp == 2:
                bull = Hero_bullet(self.x, self.y, self.target_x, self.target_y)
            else:
                bull = Hero_bullet(self.x, self.y, s_x, s_y)
            bullets.append(bull)
            self.cd = 10
            
    def ability(self):
        global h1_ab, h2_ab
        if self.tp == 1 and not GG_1:
            bull = Hero_bullet(self.x, self.y, self.x + 100, self.y)
            bullets.append(bull)
            bull = Hero_bullet(self.x, self.y, self.x - 100, self.y)
            bullets.append(bull)
            bull = Hero_bullet(self.x, self.y, self.x, self.y + 100)
            bullets.append(bull)
            bull = Hero_bullet(self.x, self.y, self.x, self.y - 100)
            bullets.append(bull)
            bull = Hero_bullet(self.x, self.y, self.x + 100, self.y + 100)
            bullets.append(bull)
            bull = Hero_bullet(self.x, self.y, self.x - 100, self.y - 100)
            bullets.append(bull)
            bull = Hero_bullet(self.x, self.y, self.x - 100, self.y + 100)
            bullets.append(bull)
            bull = Hero_bullet(self.x, self.y, self.x + 100, self.y - 100)
            bullets.append(bull)
            bull = Hero_bullet(self.x, self.y, self.x + 50, self.y + 100)
            bullets.append(bull)
            bull = Hero_bullet(self.x, self.y, self.x - 50, self.y - 100)
            bullets.append(bull)
            bull = Hero_bullet(self.x, self.y, self.x - 50, self.y + 100)
            bullets.append(bull)
            bull = Hero_bullet(self.x, self.y, self.x + 50, self.y - 100)
            bullets.append(bull)
            bull = Hero_bullet(self.x, self.y, self.x + 100, self.y + 50)
            bullets.append(bull)
            bull = Hero_bullet(self.x, self.y, self.x - 100, self.y - 50)
            bullets.append(bull)
            bull = Hero_bullet(self.x, self.y, self.x - 100, self.y + 50)
            bullets.append(bull)
            bull = Hero_bullet(self.x, self.y, self.x + 100, self.y - 50)
            bullets.append(bull)
            h1_ab = 60
        elif not GG_2:
            bull = Hero_bullet(self.x, self.y, self.target_x, self.target_y, 40, True)
            bullets.append(bull)
            h2_ab = 120
            
    def draw(self):
        if aim or self.tp == 2:
            for num, i in enumerate(npc):
                x, y = i.x, i.y
                if num == 0:
                    self.target_x, self.target_y = x, y
                if sqrt((self.x - x) ** 2 + (self.y - y) ** 2) < sqrt((self.x - self.target_x) ** 2 + (self.y - self.target_y) ** 2):
                    self.target_x, self.target_y = x, y
                self.angle = int(asin((self.target_y - self.y) / sqrt((self.x - self.target_x) ** 2 + (self.y - self.target_y) ** 2)) / pi * 180)
        else:
            self.angle = int(asin((self.target_y - self.y) / sqrt((self.x - self.target_x) ** 2 + (self.y - self.target_y) ** 2)) / pi * 180)

        if len(npc) == 0 and aim:
            self.target_x, self.target_y = self.nx * 1000, self.y
            if self.nx == -1:
                g_l_r = self.typer_l.get_rect(
                    topleft=(self.x, self.y))
                screen.blit(self.typer_l, g_l_r)
                if not ((GG_1 == True and self.tp == 1) or (GG_2 == True and self.tp == 2)):
                    g_l_r = self.curr_weapon[1].get_rect(
                        topleft=(self.x + 22 - (self.tp - 1) * 5, self.y + 42 - (self.tp - 1) * 5))
                    rot_image = pygame.transform.rotate(self.curr_weapon[1], 0)
                    rot_rect = rot_image.get_rect(center=g_l_r.center)
                    rot_image.set_colorkey((24, 29, 35))
                    screen.blit(rot_image, rot_rect)
            else:
                g_l_r = self.typer_r.get_rect(
                    topleft=(self.x, self.y))
                screen.blit(self.typer_r, g_l_r)
                if not ((GG_1 == True and self.tp == 1) or (GG_2 == True and self.tp == 2)):
                    g_l_r = self.curr_weapon[0].get_rect(
                        topleft=(self.x + 22 - (self.tp - 1) * 5, self.y + 42 - (self.tp - 1) * 5))
                    rot_image = pygame.transform.rotate(self.curr_weapon[0], 0)
                    rot_rect = rot_image.get_rect(center=g_l_r.center)
                    rot_image.set_colorkey((24, 29, 35))
                    screen.blit(rot_image, rot_rect)
        else:
            if self.target_x < self.x:
                g_l_r = self.typer_l.get_rect(
                    topleft=(self.x, self.y))
                screen.blit(self.typer_l, g_l_r)
                if not ((GG_1 == True and self.tp == 1) or (GG_2 == True and self.tp == 2)):
                    g_l_r = self.curr_weapon[1].get_rect(
                        topleft=(self.x + 22 - (self.tp - 1) * 5, self.y + 42 - (self.tp - 1) * 5))
                    rot_image = pygame.transform.rotate(self.curr_weapon[1], int(1 * self.angle))
                    rot_rect = rot_image.get_rect(center=g_l_r.center)
                    rot_image.set_colorkey((24, 29, 35))
                    screen.blit(rot_image, rot_rect)
            else:
                g_l_r = self.typer_r.get_rect(
                    topleft=(self.x, self.y))
                screen.blit(self.typer_r, g_l_r)
                if not (GG_1 == True and self.tp == 1) or (GG_2 == True and self.tp == 2):
                    g_l_r = self.curr_weapon[0].get_rect(
                        topleft=(self.x + 22 - (self.tp - 1) * 5, self.y + 42 - (self.tp - 1) * 5))
                    rot_image = pygame.transform.rotate(self.curr_weapon[0], int(-1 * self.angle))
                    rot_rect = rot_image.get_rect(center=g_l_r.center)
                    rot_image.set_colorkey((24, 29, 35))
                    screen.blit(rot_image, rot_rect)

npc_shoot = 0
pygame.init()
pygame.display.set_caption('Soul Knight: PC Edition')
size = width, height = 1200, 900
screen = pygame.display.set_mode(size)
x_pos, y_pos = 0, 0
running = True
x_pos = 0
r = 0
v = 100  
clock = pygame.time.Clock()
fps = 60
hero = Hero(1)
hero_2 = Hero(2)
waves_count = 0
waves = 3
freeze_waves = 0
win = 0
GG_1, GG_2 = False, False
pygame.mixer.music.load('grobik.mp3')
ccc = 0
hero_2.cd = cd = 0
h1_ab = 60
h2_ab = 120
room = 1
rs = 0
writing = False
f = open('earning.txt').read().split('\n')
hero.hp = int(f[0])
hero_2.hp = int(f[1])
coins = int(f[2])
if hero.hp == 0:
    hero.hp = 1
elif hero_2.hp == 0:
    hero_2.hp = 1
while running:
    if hero.cd > 0:
        hero.cd -= 1
    if hero_2.cd > 0:
        hero_2.cd -= 1
    if h1_ab > 0:
        h1_ab -= 1
    if h2_ab > 0:
        h2_ab -= 1
    if not (GG_1 and GG_2):
        npc_shoot += 1
    screen.fill((0, 0, 0))
    for a in range(1):
        for b in range(1):
            g_l_r = pol.get_rect(
                topleft=(a * 30, b * 30))
            screen.blit(pol, g_l_r)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if not (GG_1 and GG_2):
            if event.type == pygame.MOUSEMOTION:
                if not aim:
                    s_x, s_y = event.pos
                    hero.target(s_x - 50, s_y - 50)
            if event.type == pygame.MOUSEBUTTONUP:
                s_x, s_y = event.pos
                hero.shoot(s_x - 50, s_y - 50)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] == True:
                hero_2.shoot()
            if keys[pygame.K_LSHIFT] == True and h2_ab == 0:
                hero_2.ability()
            if keys[pygame.K_RSHIFT] == True and h1_ab == 0:
                hero.ability()
            if keys[pygame.K_a] == True and keys[pygame.K_s] == True:
                hero_2.move(-15, 15)
            elif keys[pygame.K_d] == True and keys[pygame.K_s] == True:
                hero_2.move(15, 15)
            elif keys[pygame.K_a] == True and keys[pygame.K_w] == True:
                hero_2.move(-15, -15)
            elif keys[pygame.K_d] == True and keys[pygame.K_w] == True:
                hero_2.move(15, -15)
            elif keys[pygame.K_a] == True:
                hero_2.move(-15, 0)
            elif keys[pygame.K_d] == True:
                hero_2.move(15, 0)
            elif keys[pygame.K_s] == True:
                hero_2.move(0, 15)
            elif keys[pygame.K_w] == True:
                hero_2.move(0, -15)
            if keys[pygame.K_LEFT] == True and keys[pygame.K_DOWN] == True:
                hero.move(-15, 10)
            elif keys[pygame.K_RIGHT] == True and keys[pygame.K_DOWN] == True:
                hero.move(15, 15)
            elif keys[pygame.K_LEFT] == True and keys[pygame.K_UP] == True:
                hero.move(-15, -15)
            elif keys[pygame.K_RIGHT] == True and keys[pygame.K_UP] == True:
                hero.move(15, -15)
            elif keys[pygame.K_LEFT] == True:
                hero.move(-15, 0)
            elif keys[pygame.K_RIGHT] == True:
                hero.move(15, 0)
            elif keys[pygame.K_DOWN] == True:
                hero.move(0, 15)
            elif keys[pygame.K_UP] == True:
                hero.move(0, -15)
            if keys[pygame.K_q] == True:
                aim = not aim
            if keys[pygame.K_RETURN] == True:
                if room == 3:
                    if hero.x in list(range(450, 650)) and hero.y in list(range(200, 500)) and not GG_1:
                        running = False
                    elif hero_2.x in list(range(450, 650)) and hero_2.y in list(range(200, 500)) and not GG_2:
                        running = False
                elif room == 1:
                    if hero.x in list(range(0, 200)) and hero.y in list(range(0, 250)) and not GG_1:
                        if coins >= 15:
                            coins -= 15
                            GG_1 = False
                            GG_2 = False
                            hero.hp = 10
                            hero_2.hp = 10
                        else:
                            t = n.render('Not enough coins!', True, (255, 0, 0))
                            screen.blit(t, (300, 550))
                    elif hero_2.x in list(range(0, 200)) and hero_2.y in list(range(0, 250)) and not GG_2:
                        if coins >= 15:
                            coins -= 15
                            GG_1 = False
                            GG_2 = False
                            hero.hp = 10
                            hero_2.hp = 10
                        else:
                            t = n.render('Not enough coins!', True, (255, 0, 0))
                            screen.blit(t, (300, 550))
    if len(npc) == 0 and waves_count < waves and room == 2:
        if freeze_waves >= 90:
            npc = []
            for i in range(choice(list(range(5 + waves_count * 2, 12 + waves_count)))):
                x_pos, y_pos = randint(50, 1100), randint(50, 700)
                ball = Goblin(x_pos, y_pos)
                npc.append(ball)
            waves_count += 1
            writing = False
        else:
            freeze_waves += 1
            writing = True
            npc_shoot = 1
            
    elif room == 2:
        freeze_waves = 0
        writing = False

    
    g_l_r = wall_hor.get_rect(
            topleft=(0, 0))
    screen.blit(wall_hor, g_l_r)
    g_l_r2 = wall_ver.get_rect(
            topleft=(0, 3))
    screen.blit(wall_ver, g_l_r2)
    g_l_r3 = wall_ver.get_rect(
            topleft=(1165, 3))
    screen.blit(wall_ver, g_l_r3)
    g_l_r1 = wall_hor.get_rect(
            topleft=(0, 747))
    screen.blit(wall_hor, g_l_r1)
    if room == 1:
        g_l_r1 = trade.get_rect(
                topleft=(35, 0))
        screen.blit(trade, g_l_r1)
    if not(len(npc) == 0 and waves_count == 3) and room == 2:
        g_l_r1 = walkthrough.get_rect(
                topleft=(350, -11))
        screen.blit(walkthrough, g_l_r1)
        g_l_r1 = walkthrough.get_rect(
                topleft=(350, 738))
        screen.blit(walkthrough, g_l_r1)
    else:
        if room != 3:
            pygame.draw.rect(screen, (125, 96, 48), (350, 0, 465, 55))
        if room != 1:
            pygame.draw.rect(screen, (125, 96, 48), (350, 740, 465, 60))
    if room == 2:
        for i in courpses:
            g_l_r2 = courpse.get_rect(
                topleft=(i[0], i[1]))
            screen.blit(courpse, g_l_r2)
    if room == 3:
        g_l_r2 = portal.get_rect(
            topleft=(500, 300))
        screen.blit(portal, g_l_r2)
            
    hero.draw()
    hero_2.draw()
    pygame.draw.rect(screen, (0, 0, 0), (0, 800, 1200, 100))
    g_l_r1 = hp_bar.get_rect(
            topleft=(100, 810))
    screen.blit(hp_bar, g_l_r1)
    g_l_r1 = hero_r.get_rect(
            topleft=(10, 810))
    screen.blit(hero_r, g_l_r1)
    pygame.draw.rect(screen, (255, 0, 0), (174, 830, int(230 * (hero.hp / hero.total)), 34))
    g_l_r1 = hp_bar.get_rect(
            topleft=(600, 810))
    screen.blit(hp_bar, g_l_r1)
    g_l_r1 = other_hero_r.get_rect(
            topleft=(510, 810))
    screen.blit(other_hero_r, g_l_r1)
    g_l_r1 = coin.get_rect(
            topleft=(1000, 810))
    screen.blit(coin, g_l_r1)
    n = pygame.font.Font(None, 80)
    t = n.render(str(coins), True, (255, 255, 0))
    screen.blit(t, (1080, 820))
    pygame.draw.rect(screen, (255, 0, 0), (674, 830, int(230 * (hero_2.hp / hero.total)), 34))
    pygame.draw.rect(screen, (0, 255, 0), (420, 820, 30, 60 - int(h1_ab)))
    pygame.draw.rect(screen, (0, 255, 0), (920, 820, 30, 60 - int(h2_ab / 2)))
    if room == 2:
        for num, x in enumerate(npc):
            x.move(x.hp, (GG_1 and GG_2))
            if not (GG_1 and GG_2):
                if x.hp <= 0:
                    del npc[num]
                    coins += 1
                    print(coins)
                if npc_shoot % x.cd  == 0:
                    x.attack()
    for num, i in enumerate(bullets):
        if i.draw() is True:
            del bullets[num]
    if room == 2:
        for num, i in enumerate(npc_bullets):
            if i.draw() is True:
                del npc_bullets[num]
    
    
    if waves_count == waves and len(npc) == 0 and win >= 0 and win < 60:
        win += 1
        n = pygame.font.Font(None, 120)
        t = n.render('ROOM COMPLETED!', True, (0, 255, 0))
        screen.blit(t, (200, 420))
    if writing:
        n = pygame.font.Font(None, 120)
        t = n.render(f'Wave {waves_count + 1}: ', True, (255, 0, 0))
        screen.blit(t, (450, 400))
    if GG_1 and GG_2:
        hero_2.typer_l, hero_2.typer_r, hero.typer_l, hero.typer_r = hc, hc, hc, hc
        n = pygame.font.Font(None, 240)
        t = n.render(f'YOU LOSE !!!', True, (255, 50, 50))
        screen.blit(t, (80, 300))
        if ccc == 0:
            pygame.mixer.music.play()
            ccc += 1
    if GG_1:
        hero.typer_l, hero.typer_r = hc, hc
    elif not GG_1:
        hero.typer_l, hero.typer_r = hero_l, hero_r
    if GG_2:
        hero_2.typer_l, hero_2.typer_r = hc, hc
    elif not GG_2:
        hero_2.typer_l, hero_2.typer_r = other_hero_l, other_hero_r
    if room == 1 and hero.x in list(range(0, 200)) and hero.y in list(range(0, 250)):
        n = pygame.font.Font(None, 120)
        t = n.render('Press ENTER to', True, (0, 255, 0))
        screen.blit(t, (200, 220))
        t = n.render('Retire HP for 15 coins.', True, (0, 255, 0))
        screen.blit(t, (200, 420))
    elif room == 1 and hero_2.x in list(range(0, 200)) and hero_2.y in list(range(0, 250)):
        n = pygame.font.Font(None, 120)
        t = n.render('Press ENTER to', True, (0, 255, 0))
        screen.blit(t, (200, 220))
        t = n.render('Retire HP for 15 coins.', True, (0, 255, 0))
        screen.blit(t, (200, 420))
    if ((not GG_1 or not GG_2) and waves_count == waves and len(npc) == 0 and room == 2) or room == 1 or (len(courpses) > 0 and waves_count == 3 and len(npc) == 0 and room == 2):
        if hero.x in list(range(350, 350 + 465)) and hero.hp > 0 and hero.y in list(range(0, 65)):
            room += 1
            hero.x = 350
            hero.y = 600
            hero_2.x = 700
            hero_2.y = 600
        if hero_2.x in list(range(350, 350 + 465)) and hero_2.hp > 0 and hero_2.y in list(range(0, 65)):
            room += 1
            hero.x = 350
            hero.y = 600
            hero_2.x = 700
            hero_2.y = 600
    if ((not GG_1 or not GG_2) and waves_count == waves and len(npc) == 0 and room == 2) or room == 3 or (len(courpses) > 0 and waves_count == 3 and len(npc) == 0 and room == 2):
        if hero.x in list(range(350, 350 + 465)) and hero.hp > 0 and hero.y in list(range(620, 800)):
            room -= 1
            hero.x = 350
            hero.y = 200
            hero_2.x = 700
            hero_2.y = 200
        if hero_2.x in list(range(350, 350 + 465)) and hero_2.hp > 0 and hero_2.y in list(range(620, 800)):
            room -= 1
            hero.x = 350
            hero.y = 200
            hero_2.x = 700
            hero_2.y = 200
    if room == 3 and hero_2.x in list(range(450, 650)) and hero_2.y in list(range(200, 500)):
        n = pygame.font.Font(None, 120)
        t = n.render('Press ENTER to', True, (0, 255, 0))
        screen.blit(t, (250, 220))
        t = n.render('teleport foreward.', True, (0, 255, 0))
        screen.blit(t, (250, 520))
    if room == 3 and hero.x in list(range(450, 650)) and hero.y in list(range(200, 500)):
        n = pygame.font.Font(None, 120)
        t = n.render('Press ENTER to', True, (0, 255, 0))
        screen.blit(t, (250, 220))
        t = n.render('teleport foreward.', True, (0, 255, 0))
        screen.blit(t, (250, 520))
    if rs >= 0 and rs < 60 and room == 1:
        rs += 1
        n = pygame.font.Font(None, 120)
        t = n.render('LEVEL 1-3!', True, (0, 0, 255))
        screen.blit(t, (350, 420))
        
    clock.tick(fps)
    pygame.display.flip()
try:
    with open("earning.txt", 'w'):
        pass
except IOError:
    pass
w = open("earning.txt", 'w')
w.write(str(hero.hp) + '\n')
w.write(str(hero_2.hp) + '\n')
w.write(str(coins) + '\n')
w.close()
import pygraph_4
