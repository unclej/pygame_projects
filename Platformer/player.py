import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, images):
        super().__init__()
        self.images = images
        self.image = images['p1_stand']
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.left = x
        self.dx = 0
        self.dy = 0
        self.facing = "R"
        self.jumping = True
        self.jump_speed = -14

    def update(self, frame, platforms):
        if self.dx ==0 and self.dy == 0 and not self.jumping:
            self.image = self.images['p1_stand']
        elif not self.jumping:
            self.image = self.images['p1_walk{}'.format(frame)]
        else:
            self.image = self.images['p1_jump']
        if self.facing == "L":
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect.x += self.dx
        #collision code for hitting the side of a platform (unused)
        '''hit_list = pygame.sprite.spritecollide(self,platforms,False)
        for plat in hit_list:
            if self.dx > 0:
                self.rect.right = plat.rect.left
            elif self.dx < 0:
                self.rect.left = plat.rect.right'''
        self.dx = 0
        if self.rect.right < 0:
            self.rect.left = 850
        elif self.rect.left > 850:
            self.rect.right = 0

        self.rect.y += self.dy
        if self.rect.top < 100:
            self.rect.top = 100
            for plat in platforms.sprites():
                plat.scroll(-1*self.dy)
        elif self.rect.top > 400:
            self.rect.top = 400
            for plat in platforms.sprites():
                if plat.rect.bottom > 0:
                    plat.scroll(-1*self.dy)
                else:
                    platforms.remove(plat)
                    if len(platforms) == 0:
                        return True
        hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for plat in hit_list:
            if self.dy > 0 and abs(self.rect.bottom - plat.rect.top)< self.dy+2:
                self.rect.bottom = plat.rect.top
                self.jumping = True
                self.dy = self.jump_speed
        #code for falling off platforms (unused)
        '''self.rect.y += 2
        hit_list = pygame.sprite.spritecollide(self, platforms, False)
        if len(hit_list) == 0:
            self.jumping = True
        else:
            for plat in hit_list:
                if abs(self.rect.bottom - plat.rect.top)> 2:
                    self.jumping = True
                else:
                    self.jumping = False
                    self.rect.y -= 2
                    break'''
        if self.jumping:
            self.dy += .5


    def left(self):
        self.facing = 'L'
        self.dx = -6

    def right(self):
        self.facing = "R"
        self.dx = 6

    def jump(self):
        self.jumping = True
        self.dy = self.jump_speed
