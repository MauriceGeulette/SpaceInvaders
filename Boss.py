import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Boss(pygame.sprite.Sprite):
    def __init__(self, p_win, p_boss_image):
        pygame.sprite.Sprite.__init__(self)
        self.winWidth = p_win.get_width()
        self.winHeight = p_win.get_height()
        self.image = p_boss_image.convert()
        self.image.set_colorkey(BLACK)
        #self.image.fill(p_color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.winWidth)
        self.rect.y = -0
        self.speedX = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedX
        if self.rect.top > self.winHeight + 10 or self.rect.left < -25 or self.rect.right > self.winWidth + 20:
            self.rect.x -= self.speedX
            self.speedX = random.randrange(-3, 3)
