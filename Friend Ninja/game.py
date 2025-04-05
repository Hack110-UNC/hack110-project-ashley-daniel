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
