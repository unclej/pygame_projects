import sys
from pygame.locals import *
from Platformer.sprite_loader import *
from Platformer.player import Player

pygame.init()
size = (width, height) = (850, 480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
speed = 1
color = (204, 0, 255)

def main():
    p1_sheet = SpriteSheet('images/p1_spritesheet.png')
    p1_file = open('images/p1_spritesheet.txt','r')
    p1_actions = {}
    sprite_list = pygame.sprite.Group()
    for line in p1_file:
        line = line.rstrip().split(" ")
        p1_actions[line[0]] = p1_sheet.get_image(int(line[2]),int(line[3]),int(line[4]),int(line[5]))
    player = Player(p1_actions)
    sprite_list.add(player)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.jump()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.left()
        if keys[pygame.K_RIGHT]:
            player.right()

        frame = (pygame.time.get_ticks()//40 %11)+1
        frame = str(frame).zfill(2)
        player.update(frame)
        screen.fill(color)
        sprite_list.draw(screen)
        pygame.display.flip()



if __name__ == "__main__":
    main()
