import pygame
import random
import sys
pygame.init()
WIDTH, NEIGHT = 600, 400,
screen = pygame.display.set_mode((WIDTH. HEIGHT))
pygame.display.set_caption("Rock paper scissors")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)
GRAY = (200, 200, 200)
BLUE = (100, 149, 237)
GREEN = (34, 139, 34)
RED = (220, 20, 60)
font = pygame.font.sysfont(None, 36)
choices = ['Rock,' "paper," "scissors"]
class Button:
    def __init__(self, x, w, h, text):
         self.rect = pygame.Rect(x, y, w, h,)
         self.text = text
    def draw(self, screen):
         pygame.draw.rect(screen. GRAY. self.rect)
         label = font.render(self.text, True, BLACK)
         