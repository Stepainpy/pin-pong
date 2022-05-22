import pygame
from random import *

pygame.init()

res = wid, hei = 600, 500
fps = 60
gray = pygame.Color('#a8a8a8')

win = pygame.display.set_mode(res)
pygame.display.set_caption('Pin-pong')
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, pl_image, x, y, wid, hie, ax, ay):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(pl_image), (wid, hie))
        self.ax = ax
        self.ay = ay
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += self.ax
        self.rect.y += self.ay

        if self.rect.y <= 0 or self.rect.y >= hei - 50:
            self.ay = -self.ay

        if pygame.sprite.collide_rect(r_l, self) or pygame.sprite.collide_rect(r_r, self):
            self.ax = -self.ax

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_o] and self.rect.y > 3:
            self.rect.y -= self.ay
        if keys[pygame.K_l] and self.rect.bottom < hei-3:
            self.rect.y += self.ay
    
    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 3:
            self.rect.y -= self.ay
        if keys[pygame.K_s] and self.rect.bottom < hei-3:
            self.rect.y += self.ay


ball = GameSprite('ball.png', 200, 200, 50, 50, 4, 4)
r_l = Player('racetka.png', 30, 200, 50, 150, 0, 4)
r_r = Player('racetka.png', 520, 200, 50, 150, 0, 4)

pygame.font.init()

font1 = pygame.font.Font(None, 35)
lose1 = font1.render('Player 1 lose', 1, (180, 0, 0))
lose2 = font1.render('Player 2 lose', 1, (180, 0, 0))

go = True
while True:
    win.fill(gray)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                if go:
                    go = False
                else:
                    go = True
    
    if go:
        r_l.update_l()
        r_r.update_r()
        ball.update()

    r_l.reset()
    r_r.reset()
    ball.reset()

    if ball.rect.right < 0:
        go = False
        win.blit(lose1, (200, 200))

    if ball.rect.x > wid:
        go = False
        win.blit(lose2, (200, 200))

    pygame.display.flip()
    clock.tick(fps)