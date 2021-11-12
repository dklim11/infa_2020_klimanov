import math
from random import choice
import random as rnd
import pygame
import numpy as np
import time

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

class ball():
    def __init__(self, screen: pygame.Surface, x = 40, y = 450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = True

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        gravitation = 1.5
        self.x += self.vx
        self.y -= self.vy

        if self.vx != 0:
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
            self.vy -= gravitation

        if self.x <= self.r:
            self.x = self.r
            self.vx = -self.vx * 0.6
            self.vy *= 0.6
            if abs(self.vx) <= 0.1:
                self.vx = 0
                self.vy = 0
                self.live = False
        if self.x >= 800 - self.r:
            self.x = 800 - self.r
            self.vy *= 0.6
            self.vx = -self.vx * 0.6
            if abs(self.vx) <= 0.01:
                self.vx = 0
                self.vy = 0
                self.live = False
        if self.y >= 550 - self.r:
            self.vy = -0.6 * self.vy
            self.vx *= 0.6
            self.y = 550 - self.r
            if abs(self.vy) <= 10:
                self.vy = 0
                self.vx = 0
                self.live = False

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.r + obj.r)**2:
            return True
        else:
            return False
    
    def destroy(self):
            pygame.draw.circle(self.screen, WHITE, (self.x, self.y), 10 * self.r)

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0] == 20:
                self.an = 90
            else:
                self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.polygon(screen, self.color, [[20, 450], 
        [20 + np.cos(self.an)*self.f2_power, 450 + np.sin(self.an)*self.f2_power], [20, 460]])
        pass

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

class Target:
    def __init__(self):
        self.screen = screen
        self.points = 0
        self.live = 1
        self.x = 500
        self.y = 400
        self.vx = 20
        self.vy = 20
        self.r = 35
        self.color = GREY

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = rnd.randint(450, 780)
        self.y = rnd.randint(100, 500)
        self.vx = rnd.randint(5, 10)
        self.vy = rnd.randint(2,5)
        self.r = rnd.randint(2, 50)
        color = self.color = RED

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def T_move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        gravitation = 1.5
        self.x += self.vx
        self.y -= self.vy

        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

        if self.x <= 100 + self.r:
            self.x = 100 + self.r
            self.vx = -self.vx
        if self.x >= 800 - self.r:
            self.x = 800 - self.r
            self.vx = -self.vx
        if self.y >= 550 - self.r:
            self.vy = -self.vy
            self.y = 550 - self.r
        if self.y <= self.r:
            self.vy = -self.vy
            self.y = self.r

    def draw(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.r, self.r)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
targets = [0] * 2


clock = pygame.time.Clock()
gun = Gun(screen)
finished = False

for i in range(2):
    targets[i] = Target()

while not finished:
    screen.fill(WHITE)
    gun.draw()

    for i in range(2):
        targets[i].T_move()
        targets[i].draw()

    for b in balls:
        if b.live:
            b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        if b.live:
            b.move()
            for i in range(2):
                if b.hittest(targets[i]) and targets[i].live:
                    targets[i].hit()
                    targets[i].new_target()
        else:
            b.destroy()
    gun.power_up()

pygame.quit()
