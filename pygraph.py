import pygame
from random import choice, randint
from math import sqrt, asin, pi, sin, cos


goblin_l = pygame.image.load('goblin_l.png')
goblin_l.set_colorkey((255, 255, 255))
goblin_r = pygame.image.load('goblin_r.png')
goblin_r.set_colorkey((255, 255, 255))
hero_l = pygame.image.load('not_bandit.png')
hero_l.set_colorkey((255, 255, 255))
hero_r = pygame.image.load('bandit.png')
hero_r.set_colorkey((255, 255, 255))
pol = pygame.image.load('pol.png')
pol.set_colorkey((255, 255, 255))
wall_hor = pygame.image.load('wall_hor.png')
wall_hor.set_colorkey((255, 255, 255))
wall_ver = pygame.image.load('wall_ver.png')
wall_ver.set_colorkey((255, 255, 255))
rifle_l = pygame.image.load('rifle_l.png')
rifle_l.set_colorkey((24, 29, 35))
rifle_r = pygame.image.load('rifle_r.png')
rifle_r.set_colorkey((24, 29, 35))
bullet = pygame.image.load('bullet.png')
bullet.set_colorkey((255, 255, 255))

aim = True


class Nepice:
    def __init__(self, x, y):
        self.nx = choice([-1, 1])
        self.ny = choice([-1, 1])
        self.y = y
        self.x = x
        self.draw()
        self.move()
        self.hp = 0

    def get_damage(self, amount):
        self.hp -= amount
            
    
    def move(self):
        self.x += self.nx * v / fps
        self.y += self.ny * v / fps
        if self.x <= 30:
            self.nx *= -1
        if self.y <= 50:
            self.ny *= -1
        if self.x > width - 100:
            self.nx *= -1
        if self.y > height - 120:
            self.ny *= -1
        self.draw()
        
    def draw(self):
        pass



class Goblin(Nepice):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.hp = 12

    def draw(self):
        if self.nx == -1:
            g_l_r = goblin_l.get_rect(
                topleft=(self.x, self.y))
            screen.blit(goblin_l, g_l_r)
        else:
            g_l_r = goblin_r.get_rect(
                topleft=(self.x, self.y))
            screen.blit(goblin_r, g_l_r)

        

            
npc = []
bullets = []


class Hero_bullet:
    def __init__(self, start_x, start_y, end_x, end_y):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
##        CHANGE TO 3!!!        
        self.damage = 1000
        self.x, self.y = self.start_x, self.start_y
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
        if self.x < 30 or self.x > 1112 or self.y < 30 or self.y > 680:
            pygame.draw.circle(screen, (255, 0, 0), (self.x + 30, self.y + 55), 15)
            return True
        for num, i in enumerate(npc):
            if int(self.x + 30) in list(range(int(i.x), int(i.x + 70))) and int(self.y + 50) in list(range(int(i.y), int(i.y + 50))):
                i.get_damage(self.damage)
                pygame.draw.circle(screen, (255, 0, 0), (self.x + 30, self.y + 55), 15)
                return True
        g_l_r = bullet.get_rect(
            topleft=(self.x + 35, self.y + 50))
        screen.blit(bullet, g_l_r)
        return False
                    

class Hero:
    def __init__(self):
        self.x = 600
        self.y = 600
        self.nx = 1
        self.weapons = [[rifle_r, rifle_l]]
        self.curr_weapon = self.weapons[0]
        self.target_x = 1000
        self.target_y = 600
        self.draw()
        self.angle = 0

    def move(self, m_x, m_y):
        if self.x + m_x <= 10:
            return
        if self.y + m_y <= 40:
            return
        if self.x + m_x > width - 100:
            return
        if self.y + m_y > height - 125:
            return
        self.x += m_x
        self.y += m_y
        if m_x < 0:
            self.nx = -1
        elif m_x > 0:
            self.nx = 1
        self.draw()

    def target(self, x, y):
        self.target_x = x
        self.target_y = y
    
    def shoot(self, s_x, s_y):
        global bullets
        if aim:
            bull = Hero_bullet(self.x, self.y, self.target_x, self.target_y)
        else:
            bull = Hero_bullet(self.x, self.y, s_x, s_y)
        bullets.append(bull)
        
    def draw(self):
        if aim:
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
                g_l_r = hero_l.get_rect(
                    topleft=(self.x, self.y))
                screen.blit(hero_l, g_l_r)
                g_l_r = self.curr_weapon[1].get_rect(
                    topleft=(self.x + 22, self.y + 42))
                rot_image = pygame.transform.rotate(self.curr_weapon[1], 0)
                rot_rect = rot_image.get_rect(center=g_l_r.center)
                rot_image.set_colorkey((24, 29, 35))
                screen.blit(rot_image, rot_rect)
            else:
                g_l_r = hero_r.get_rect(
                    topleft=(self.x, self.y))
                screen.blit(hero_r, g_l_r)
                g_l_r = self.curr_weapon[0].get_rect(
                    topleft=(self.x + 22, self.y + 42))
                rot_image = pygame.transform.rotate(self.curr_weapon[0], 0)
                rot_rect = rot_image.get_rect(center=g_l_r.center)
                rot_image.set_colorkey((24, 29, 35))
                screen.blit(rot_image, rot_rect)
        else:
            if self.target_x < self.x:
                g_l_r = hero_l.get_rect(
                    topleft=(self.x, self.y))
                screen.blit(hero_l, g_l_r)
                g_l_r = self.curr_weapon[1].get_rect(
                    topleft=(self.x + 22, self.y + 42))
                rot_image = pygame.transform.rotate(self.curr_weapon[1], int(1 * self.angle))
                rot_rect = rot_image.get_rect(center=g_l_r.center)
                rot_image.set_colorkey((24, 29, 35))
                screen.blit(rot_image, rot_rect)
            else:
                g_l_r = hero_r.get_rect(
                    topleft=(self.x, self.y))
                screen.blit(hero_r, g_l_r)
                g_l_r = self.curr_weapon[0].get_rect(
                    topleft=(self.x + 22, self.y + 42))
                rot_image = pygame.transform.rotate(self.curr_weapon[0], int(-1 * self.angle))
                rot_rect = rot_image.get_rect(center=g_l_r.center)
                rot_image.set_colorkey((24, 29, 35))
                screen.blit(rot_image, rot_rect)

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 1200, 800
    screen = pygame.display.set_mode(size)
    x_pos, y_pos = 0, 0
    running = True
    x_pos = 0
    r = 0
    v = 100  
    clock = pygame.time.Clock()
    fps = 60
    hero = Hero()
    waves_count = 0
    waves = 3
    freeze_waves = 0
    win = 0
    while running:
        screen.fill((0, 0, 0))
        for a in range(1):
            for b in range(1):
                g_l_r = pol.get_rect(
                    topleft=(a * 30, b * 30))
                screen.blit(pol, g_l_r)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                if not aim:
                    s_x, s_y = event.pos
                    hero.target(s_x, s_y)
            if event.type == pygame.MOUSEBUTTONUP:
                s_x, s_y = event.pos
                hero.shoot(s_x, s_y)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] == True and keys[pygame.K_s] == True:
                hero.move(-10, 10)
            elif keys[pygame.K_d] == True and keys[pygame.K_s] == True:
                hero.move(10, 10)
            elif keys[pygame.K_a] == True and keys[pygame.K_w] == True:
                hero.move(-10, -10)
            elif keys[pygame.K_d] == True and keys[pygame.K_w] == True:
                hero.move(10, -10)
            elif keys[pygame.K_a] == True:
                hero.move(-10, 0)
            elif keys[pygame.K_d] == True:
                hero.move(10, 0)
            elif keys[pygame.K_s] == True:
                hero.move(0, 10)
            elif keys[pygame.K_w] == True:
                hero.move(0, -10)
            if keys[pygame.K_q] == True:
                aim = not aim
        if len(npc) == 0 and waves_count < waves:
            if freeze_waves >= 90:
                npc = []
                for i in range(choice(list(range(3, 10)))):
                    x_pos, y_pos = randint(50, 1100), randint(50, 700)
                    ball = Goblin(x_pos, y_pos)
                    npc.append(ball)
                waves_count += 1
                writing = False
            else:
                freeze_waves += 1
                writing = True
                
        else:
            freeze_waves = 0
            writing = False
        g_l_r = wall_hor.get_rect(
                topleft=(0, 0))
        screen.blit(wall_hor, g_l_r)
        g_l_r1 = wall_hor.get_rect(
                topleft=(0, 747))
        screen.blit(wall_hor, g_l_r1)
        g_l_r2 = wall_ver.get_rect(
                topleft=(0, 3))
        screen.blit(wall_ver, g_l_r2)
        g_l_r3 = wall_ver.get_rect(
                topleft=(1165, 3))
        screen.blit(wall_ver, g_l_r3)
        for num, x in enumerate(npc):
            x.move()
            if x.hp <= 0:
                del npc[num]
        hero.draw()
        for num, i in enumerate(bullets):
            if i.draw() is True:
                del bullets[num]
        if waves_count == waves and len(npc) == 0 and win >= 0 and win < 60:
            win += 1
            n = pygame.font.Font(None, 120)
            t = n.render('ROOM COMPLETED!', True, (0, 255, 0))
            screen.blit(t, (200, 420))
        if writing:
            n = pygame.font.Font(None, 120)
            t = n.render(f'Wave {waves_count + 1}: ', True, (255, 0, 0))
            screen.blit(t, (450, 400))
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
