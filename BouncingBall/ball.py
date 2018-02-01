import pygame, random
from pygame.locals import *

class Ball:
    def __init__(self, screen, pos):
        self.img = pygame.image.load("../images/ball.png")
        scale = random.randint(1, 5)*10
        self.img = pygame.transform.smoothscale(self.img, (scale, scale))
        self.rect = self.img.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0, random.randint(2, 5))
        self.speed.rotate_ip(random.randint(0, 360))
        self.screen = screen

    def move(self):
        screen_info = pygame.display.Info()
        self.rect.move_ip(self.speed)
        if self.rect.left < 0:
            self.speed[0] *= -1
            self.rect.left = 0
        elif self.rect.right > screen_info.current_w:
            self.speed[0] *= -1
            self.rect.right = screen_info.current_w
        if self.rect.top < 0:
            self.speed[1] *= -1
            self.rect.top = 0
        elif self.rect.bottom > screen_info.current_h:
            self.speed[1] *= -1
            self.rect.bottom = screen_info.current_h

    def draw(self):
        self.screen.blit(self.img, self.rect)
