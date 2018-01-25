import pygame, sys
from pygame.locals import *
from ball import *

pygame.init()

size = (width, height) = (850, 480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

color = (26, 255, 255)

def main():
    ball = Ball(screen)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        ball.move(width,height)
        screen.fill(color)
        ball.draw()
        pygame.display.flip()

if __name__ == '__main__':
    main()
