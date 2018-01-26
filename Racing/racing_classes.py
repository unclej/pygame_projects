import pygame,random
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

    def __init__(self,screen,img_path):
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (75, 150))
        self.rect = self.img.get_rect()
        self.rect.move_ip(290,250)
        self.screen = screen

    def draw(self):
        self.screen.blit(self.img,self.rect)

class Obstacle:

    def __init__(self,screen,img_path,x,y):
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (50, 50))
        self.rect = self.img.get_rect()
        self.rect.move_ip(x, y)
        self.screen = screen

    def update(self,speed):
        self.rect.move_ip([0,speed])
        if(self.rect.top > self.screen.get_height()):
            self.rect.move_ip([0,-550])
            return True
        return False


    def draw(self):
        self.screen.blit(self.img, self.rect)
