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
