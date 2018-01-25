import pygame, sys
from pygame.locals import *
from racing_classes import *

pygame.init()
color = (26, 255, 255)
size = (width, height) = (850, 480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
speed = 5

def main():
    road = []
    road.append(Road(screen,"images/road1.png",0))
    road.append(Road(screen,"images/road2.png",-480))
    car = RaceCar(screen,"images/car.png")
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        for r in road:
            r.update(10)

        screen.fill(color)
        for r in road:
            r.draw()
        car.draw()
        pygame.display.flip()

if __name__ == '__main__':
    main()
