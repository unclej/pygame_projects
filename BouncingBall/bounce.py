import sys
from BouncingBall.ball import *

pygame.init()

size = (width, height) = (850, 480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

color = (26, 255, 255)
balls = []

def main():
    for i in range(10):
        balls.append(Ball(screen, width/2,height/2))
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                balls.append(Ball(screen, event.pos[0], event.pos[1]))
            if event.type == KEYDOWN:
                if event.key == K_d:
                    for i in range(len(balls)//2):
                        balls.pop(0)

        screen.fill(color)
        for ball in balls:
            ball.move(width,height)
        for ball in balls:
            ball.draw()
        pygame.display.flip()

if __name__ == '__main__':
    main()
