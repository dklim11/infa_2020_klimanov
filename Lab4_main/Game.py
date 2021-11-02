import pygame
from pygame.draw import *
from random import random
from random import randint
import numpy as np

pygame.init()

"""
Defining some constans
"""
FPS = 30
dt = 0.005
bond_h = 80
bond_x = 1000
bond_y = 700
vel = 4000
screen = pygame.display.set_mode((bond_x, bond_y))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
finished = False
Score = 0

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
screen.fill(WHITE)

def drawBall(one):
    """
    function is drawing ball after another function have already
    edited the ball`s coordinates
    """
    circle(screen, COLORS[one[5]], (one[0], one[1]), one[4], one[4])

def createBall():
    """
    Function is creating a new ordinary ball, which have random sizes on axes 
    and radius. 
    """
    x_cor = randint(0, bond_x) + 50
    y_cor = randint(0, bond_y) + 50
    vel_x = randint(0, vel) + 200
    vel_y = randint(0, vel) + 200
    radius = randint(30, 50)
    arg = randint(0, 5)
    prototype = [x_cor, y_cor, vel_x, vel_y, radius, arg, 0]
    return prototype

def collision_check(one):
    x_cor = one[0]
    y_cor = one[1]  
    radius = one[4]
    
    circle(screen, WHITE, (x_cor, y_cor), radius, radius)
    pygame.display.update()

    x_cor += one[2] * dt
    y_cor += one[3] * dt

    if one[6] == 0:
        "common aim"
        if x_cor + radius >= bond_x:
            one[2] = -vel * random()
            one[3] = one[3]/abs(one[3])*np.sqrt(vel**2 - one[2]**2)
            x_cor = bond_x - radius
        elif x_cor - radius <= 0:
            one[2] = vel * random()
            one[3] = one[3]/abs(one[3])*np.sqrt(vel**2 - one[2]**2)
            x_cor = radius

        if y_cor + radius >= bond_y:
            one[3] = -vel * random()
            one[2] = one[2]/abs(one[2])*np.sqrt(vel**2 - one[3]**2)
            y_cor = bond_y - radius
        elif y_cor - radius <= bond_h:
            one[3] = vel * random()
            one[2] = one[2]/abs(one[2])*np.sqrt(vel**2 - one[3]**2)
            y_cor = radius + bond_h
    else:
        "extraordinary aim"
        if x_cor + radius >= bond_x:
            one[2] = -one[2]
            x_cor = bond_x - radius
        elif x_cor - radius <= 0:
            one[2] = -one[2]
            x_cor = radius

        if y_cor + radius >= bond_y:
            one[3] = -one[3]
            y_cor = bond_y - radius
        elif y_cor - radius <= bond_h:
            one[3] = -one[3]
            y_cor = radius + bond_h

    return x_cor, y_cor

def updating(one, score):
    if one[6] == 1:
        f = pygame.font.Font(None, 50)
        text3 = f.render('FATALITY!!!', 1, (180, 0, 0))
        screen.blit(text3, (400, 400))
        score += 500
    else:
        score += one[4]

    circle(screen, WHITE, (one[0], one[1]), one[4], one[4])
    return score

def createBoss():
    """
    Function is creating a new Boss-ball, which have random sizes on axes 
    and radius. This ball always changes its color(arg is changing from step to step), 
    also it has another rules of reflecting from screen`s boundaries
    """
    x_cor = randint(0, bond_x) + 50
    y_cor = randint(0, bond_y) + 50
    vel_x = randint(0, vel) + 200
    vel_y = randint(0, vel) + 200
    radius = randint(50, 80)
    arg = randint(0, 5)
    prototype = [x_cor, y_cor, vel_x, vel_y, radius, arg, 1]
    return prototype

def create_by_chance():
    """
    This function makes decision what type of ball to create
    """
    if random() > 0.7:
        return createBoss()
    else:
        return createBall()

def change_color(one):
    """
    Function is changing a Boss-ball argument, that is responsible
    for color, therefore on the next step Boss-ball will be drawn
    with another color
    """
    if one[6] == 1:
        one[5] += 1
        one[5] = one[5] % 6

def update_Score():
    """
    Function is editing the score on the screen due to
    it`s relevant value
    """
    num = str(Score)
    f1 = pygame.font.Font(None, 36)
    rect(screen, (255, 255, 255), [0, 50, 200, 20], 25)
    text1 = f1.render('Score: ', 1, (180, 0, 0))
    text2 = f1.render(num, 1, (180, 0, 0))
    screen.blit(text1, (10, 40))
    screen.blit(text2, (100, 40))

def finishing(name, Score):
    """
    This function is editing the rating
    by means of inserting new string with name + Score
    on a certain position of file
    """
    Read = []
    with open('C:/Users/user/Desktop/PyProjects/Lab4/players.txt') as file:
        number_of_stop = 0
        count_string = 0

        Read += file.readlines()
        Read_prepared = []
        
        for entry in Read:
            if entry != '\n':
                Read_prepared.append(entry)

        Read = Read_prepared

        for j in range(len(Read)):
            Read[j] = Read[j][:len(Read[j]) - 1]

        for j in range(len(Read)):
            string_val = ''
            count_ = 0
            count_string += 1
            
            for i in range(len(Read[j])):
                if Read[j][i] == ' ':
                    count_ += 1
                elif count_ == 1 and Read[j][i] != '\n':
                    string_val += Read[j][i]
            
            value = 0
            for j in range(len(string_val)):
                value += int(string_val[j]) * 10**(len(string_val) - j - 1)

            if value >= Score:
                number_of_stop += 1
        Read.insert(number_of_stop, name + ' ' + str(Score))

    output = open('C:/Users/user/Desktop/PyProjects/Lab4/players.txt', 'w')
    for i in range(len(Read)):
        Read[i] += '\n'
        output.write(Read[i])
    output.close()

"""
Creating of list with balls` characteristics

Each list contains following data:
        [x_coordinate, y_coordinate, x_velocity, y_velocity,
        , radius, num of color, 1 if ball is extraordinary == Boss]
"""
number_of_balls = int(input('Введите число шаров : '))
balls = [[] for i in range(number_of_balls)]

for i in range(number_of_balls):
    balls[i] = createBall()

pygame.display.update()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            name = str(input('Введите своё имя : '))
            finishing(name, Score)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x0, y0 = event.pos
            for i in range(number_of_balls):
                if (x0 - balls[i][0])**2 + (y0 - balls[i][1])**2 <= balls[i][4]**2:
                    Score = updating(balls[i], Score)
                    balls[i] = create_by_chance()
                    pygame.display.update()

    for i in range(number_of_balls):  
        balls[i][0], balls[i][1] = collision_check(balls[i])
        change_color(balls[i])
        drawBall(balls[i])
        update_Score()
        pygame.display.update()

pygame.quit()