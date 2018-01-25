import pygame
from pygame.locals import *

class Road:

    def __init__(self,screen,img_path,y):
        self.img = pygame.image.load(img_path)
        self.rect = self.img.get_rect()
        self.y = y
        self.rect.move_ip([0,y])
        self.screen = screen

    def update(self,speed):
        self.y += speed
        self.rect.move_ip([0,speed])
        if(self.rect.top > self.screen.get_height()):
            self.y = 0 - self.screen.get_height()*2
            self.rect.move_ip([0, self.y])

    def draw(self):
        self.screen.blit(self.img, self.rect)

class RaceCar:

    def __init__(self,img_path):
        self.img = pygame.image.load(img_path)
        self.rect = self.img.get_rect()
