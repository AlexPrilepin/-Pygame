import pygame
from random import choice, randint


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



class Nepice:
    def __init__(self, x, y):
        self.nx = choice([-1, 1])
        self.ny = choice([-1, 1])
        self.y = y
        self.x = x
        self.draw()
        self.move()

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
##        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 10, 30), 10)
        pass



class Goblin(Nepice):
    def __init__(self, x, y):
        super().__init__(x, y)

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


class Hero:
    def __init__(self):
        self.x = 600
        self.y = 600
        self.nx = 1
        self.draw()

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
        
    def draw(self):
        if self.nx == -1:
            g_l_r = hero_l.get_rect(
                topleft=(self.x, self.y))
            screen.blit(hero_l, g_l_r)
        else:
            g_l_r = hero_r.get_rect(
                topleft=(self.x, self.y))
            screen.blit(hero_r, g_l_r)
        

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
    for i in range(choice(list(range(1, 10)))):
        x_pos, y_pos = randint(50, 1100), randint(50, 700)
        ball = Nepice(x_pos, y_pos)
        npc.append(ball)
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
            if event.type == pygame.MOUSEBUTTONUP:
                npc = []
                for i in range(choice(list(range(3, 10)))):
                    x_pos, y_pos = randint(50, 1100), randint(50, 700)
                    ball = Goblin(x_pos, y_pos)
                    npc.append(ball)
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
        for x in npc:
            x.move()
        hero.draw()
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



        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
