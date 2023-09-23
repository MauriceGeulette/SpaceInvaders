import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Meteor(pygame.sprite.Sprite):
    def __init__(self, p_win, p_meteor_images):
        pygame.sprite.Sprite.__init__(self)
        self.winWidth = p_win.get_width()
        self.winHeight = p_win.get_height()
        self.image = random.choice(p_meteor_images).convert()
        self.image.set_colorkey(BLACK)
        #self.image.fill(p_color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.winWidth)
        self.rect.y = random.randrange(-100, -40)
        self.speedY = random.randrange(1, 8)
        self.speedX = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        if self.rect.top > self.winHeight + 10 or self.rect.left < -25 or self.rect.right > self.winWidth + 20:
            self.rect.x = random.randrange(self.winWidth)
            self.rect.y = random.randrange(-100, -40)
            self.speedY = random.randrange(1, 8)
            self.speedX = random.randrange(-3, 3)
