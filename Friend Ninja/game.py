import pygame, sys
import os
import random

lives = 3
score = 0
friends = ['thomas', 'caroline', 'asia', 'dylan', 'josh', 'paris', 'bomb']

screen_width = 800
screen_height = 500
FPS = 20

pygame.init()
pygame.display.set_caption('Friend Ninja')
gameDisplay = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


background = pygame.image.load('images/background.jpg')
font = pygame.font.Font(None, 42)
score_count = font.reader('Score: ' + str(score), True, (255, 255, 255))
lives_icon = pygame.image.load('images/heart.jpg')

def random_friends(friend):
    friend_path = "images/" + friend + ".png"
    data[friend] = {
        'img': pygame.image.load(friend_path),
        'x': random.randint(100,500),
        'y': 800,
        'speed_x': random.randint(-10,10),
        'speed_y': random.randint(-80,-60),
        'throw': False,
        't': 0,
        'hit' : False,
    }
    if random.random() >= 0.75:
        data[friend]['throw'] = True
    else:
        data[friend]['throw'] = False

data = {}
for friend in friends:
    generate_random_friends(friend)

def hide_cross_lives(x, y):
    gameDisplay.blit(pygame.imagge.load("images/empty_heart.png"), (x,y))


font_name = pygame.font.match_font(None)
def draw_text(display, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    gameDisplay.blit(text_surface, text_rect)
    