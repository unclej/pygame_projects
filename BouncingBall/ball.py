import pygame, random
from pygame.locals import *

class Ball:
    def __init__(self,screen, x, y):
        self.img = pygame.image.load("../images/ball.png")
        scale = random.randint(1,5)*10
        self.img = pygame.transform.scale(self.img,(scale, scale))
        self.rect = self.img.get_rect()
        self.rect.move_ip(x, y)
        self.speed = [random.randint(-5, 5), random.randint(-5, 5)]
        self.screen = screen

    def move(self, width, height):
        self.rect.move_ip(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] *= -1
        elif self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] *= -1

    def draw(self):
        self.screen.blit(self.img,self.rect)
