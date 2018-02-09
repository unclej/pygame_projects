import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, images):
        super().__init__()
        self.images = images
        self.image = images['p1_jump']
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.left = x
        self.dx = 0
        self.dy = 0
        self.facing = "R"
        self.jump_speed = -14
        self.world_y = pygame.display.Info().current_h-y
        self.progress = 0

    def update(self, platforms):
        screen_info = pygame.display.Info()

        #update the image direction
        self.image = self.images['p1_jump']
        if self.facing == "L":
            self.image = pygame.transform.flip(self.image, True, False)
        #handle left/right movement
        self.rect.x += self.dx
        self.dx = 0

        if self.rect.right < 0:
            self.rect.left = screen_info.current_w
        elif self.rect.left > screen_info.current_w:
            self.rect.right = 0
        #handle vertical movement
        self.rect.y += self.dy
        self.world_y += self.dy*-1
        if self.world_y > self.progress:
            self.progress = self.world_y
        #scroll platforms down
        if self.rect.top < 100:
            self.rect.top = 100
            for plat in platforms.sprites():
                plat.scroll(-1*self.dy)
        #scroll platforms up (player fell off world)
        elif self.rect.top > screen_info.current_h-80:
            self.rect.top = screen_info.current_h-80
            for plat in platforms.sprites():
                if plat.rect.bottom > 0:
                    plat.scroll(-1*self.dy)
                else:
                    plat.kill()
            return True

        #check if the player hit any platforms
        hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for plat in hit_list:
            #player landed on top of a platform
            if self.dy > 0 and abs(self.rect.bottom - plat.rect.top)< self.dy+2:
                self.rect.bottom = plat.rect.top
                self.dy = self.jump_speed
        #gravity
        self.dy += .5

    def left(self):
        self.facing = 'L'
        self.dx = -6

    def right(self):
        self.facing = "R"
        self.dx = 6
