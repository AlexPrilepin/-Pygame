import pygame
from random import choice, randint

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
        if self.y <= 30:
            self.ny *= -1
        if self.x > width - 60:
            self.nx *= -1
        if self.y > height - 60:
            self.ny *= -1
        self.draw()
        
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 10, 30), 10)

            
npc = []


class Hero:
    def __init__(self):
        self.x = 600
        self.y = 600
        self.draw()

    def move(self, m_x, m_y):
        if self.x + m_x <= 30:
            return
        if self.y + m_y <= 30:
            return
        if self.x + m_x > width - 60:
            return
        if self.y + m_y > height - 60:
            return
        self.x += m_x
        self.y += m_y
        self.draw()
        
    def draw(self):
        pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), 10)

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                npc = []
                for i in range(choice(list(range(3, 10)))):
                    x_pos, y_pos = randint(50, 1100), randint(50, 700)
                    ball = Nepice(x_pos, y_pos)
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
        for a in range(0, 120, 4):
            pygame.draw.rect(screen, (0, 255, 0), (a * 10 + 1, 0, 25, 25))
            pygame.draw.rect(screen, (255, 0, 0), (a * 10 + 4, 3, 21, 21), 3)
            pygame.draw.rect(screen, (0, 255, 0), (a * 10 + 1, 772, 25, 25))
            pygame.draw.rect(screen, (255, 0, 0), (a * 10 + 4, 777, 20, 18), 3)
            pygame.draw.rect(screen, (0, 255, 0), (0, a * 10 + 1, 25, 25))
            pygame.draw.rect(screen, (255, 0, 0), (3, a * 10 + 4, 21, 21), 3)
            pygame.draw.rect(screen, (0, 255, 0), (1172, a * 10 + 1, 25, 25))
            pygame.draw.rect(screen, (255, 0, 0), (1177, a * 10 + 4, 18, 20), 3)


        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
