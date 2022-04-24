import pygame
from random import *

pygame.init()

res = wid, hei = 800, 600
fps = 60
gray = pygame.Color('#a8a8a8')

win = pygame.display.set_mode(res)
pygame.display.set_caption('Pin-pong')
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, pl_image, x, y, wid, hie, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(pl_image), (wid, hie))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

go = True
while True:
    win.fill(gray)
    [exit() for i in pygame.event.get() if i.type == pygame.QUIT]
    
    if go:
        pass

    pygame.display.flip()
    clock.tick(fps)