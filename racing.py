import pygame, sys
from pygame.locals import *
from racing_classes import *

pygame.init()
size = (width, height) = (850, 480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
speed = 1

def main():
    global speed
    road = []
    road.append(Road(screen,"images/road1.png",0))
    road.append(Road(screen,"images/road2.png",-480))
    car = RaceCar(screen,"images/car.png")
    obstacles = []
    for i in range(4):
        obstacles.append(Obstacle(screen, "images/cone.png", 150 + i * 50, -280))
        obstacles.append(Obstacle(screen,"images/cone.png",360+i*50, -30))
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        for r in road:
            r.update(speed)
            r.draw()

        for o in obstacles:
            if(o.update(speed)):
                pass
            else:
                o.draw()
        car.draw()
        pygame.display.flip()

if __name__ == '__main__':
    main()
