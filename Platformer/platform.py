import pygame, random

class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, img_path, width=70, height=70):
        super().__init__()
        self.image = pygame.Surface([width, height]).convert()
        self.image.blit(pygame.image.load(img_path).convert(), (0, 0), (0, 0, width, height))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

    def scroll(self,change):
        self.rect.top += change
        if self.rect.top > 480:
            self.rect.top = -50
            self.rect.left = random.randint(5,80)*10
