import pygame
from pygame.locals import *

class Ball:
    def __init__(self,screen):
        self.img = pygame.image.load("../images/ball.gif")
        self.img = pygame.transform.scale(self.img,(20,20))
        self.rect = self.img.get_rect()
        self.rect.move_ip(320, 200)
        self.speed = [2, -2]
        self.screen = screen

    def move(self,width,height):
        self.rect.move_ip(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] *= -1
            self.rect.move_ip(self.speed)
        elif self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] *= -1
            self.rect.move_ip(self.speed)

    def draw(self):
        self.screen.blit(self.img,self.rect)
