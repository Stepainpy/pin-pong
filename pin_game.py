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
        self.wid = wid
        self.hie = hie
        self.image = pygame.transform.scale(pygame.image.load(pl_image), (self.wid, self.hie))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x = randint(0, 800)
        self.rect.y = randint(0, 600)

        self.wid = randint(0, 500)
        self.hie = randint(0, 500)

ball = GameSprite('ball.png', 100, 100, 100, 100, 0)

go = True
while True:
    win.fill(gray)
    [exit() for i in pygame.event.get() if i.type == pygame.QUIT]
    
    ball.update()
    ball.reset()

    pygame.display.flip()
    clock.tick(fps)