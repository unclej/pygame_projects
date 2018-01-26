import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self,images):
        super().__init__()
        self.images = images
        self.image = images['p1_stand']
        self.rect = self.image.get_rect()
        self.rect.bottom = 450
        self.rect.left = 400
        self.dx = 0
        self.dy = 0
        self.facing = "R"
        self.jumping = False

    def update(self, frame):
        if self.dx ==0 and self.dy == 0:
            self.image = self.images['p1_stand']
        elif not self.jumping:
            self.image = self.images['p1_walk{}'.format(frame)]
        else:
            self.image = self.images['p1_jump']
        if self.facing == "L":
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect.x += self.dx
        self.dx = 0

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 850:
            self.rect.right = 850

        self.rect.y += self.dy
        if(self.rect.bottom < 450):
            self.dy += .5
        else:
            self.rect.bottom = 450
            self.jumping = False
            self.dy = 0

    def left(self):
        self.facing = 'L'
        self.dx = -6

    def right(self):
        self.facing = "R"
        self.dx = 6

    def jump(self):
        self.jumping = True
        self.dy = -10
