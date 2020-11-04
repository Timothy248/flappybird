import pygame
import variables as v


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.x = 0
        self.y = 0

        self.originalImage = pygame.image.load("bird.png")
        self.image = self.originalImage
        self.rect = self.image.get_rect()

        self.velY = 0
        self.dead = False

    def move(self):
        if not self.dead:
            self.velY += v.gravity
            self.velY = min(25, max(-1000, self.velY))
        else:
            self.velY += 1
            self.velY = min(40, max(-1000, self.velY))

    def update(self):
        if not self.dead:
            self.rect.move_ip(0, self.velY)
            self.move()

            if self.rect.centery > v.gameSize[1] - self.image.get_height():
                self.rect.centery = v.gameSize[1] - self.image.get_height()

            if self.rect.centery < self.image.get_height() / 2 - 1:
                self.rect.centery = self.image.get_height() / 2 - 1
                self.velY += 0.1
        else:
            self.rect.move_ip(2, self.velY)
            self.move()

    def flap(self):
        if not self.dead:
            self.velY -= v.flapHeight
            self.velY = min(20, max(-9.5, self.velY))

    def rotate(self, tilt):
        self.image = pygame.transform.rotate(self.originalImage, tilt)

    def die(self):
        self.dead = True
        self.velY -= 4000
        self.velY = min(20, max(-9, self.velY))
