import pygame
import pipe as p
import variables as v
from random import randint


class PipePair(pygame.sprite.Sprite):
    def __init__(self, startingPosition, screen):
        super().__init__()

        self.gap = v.gap / 2
        self.minDistanceEdge = 130

        self.screen = screen

        self.pipe0 = p.Pipe(True, startingPosition)
        self.pipe1 = p.Pipe(False, startingPosition)

        self.pairMiddle = 0
        self.random = 0

        self.stop = False

        self.pair()

    def pair(self):
        self.random = randint(0 + self.minDistanceEdge, v.gameSize[1] - self.minDistanceEdge)

        self.pipe0.setPosition(v.gameSize[1] - self.random - self.gap)
        self.pipe1.setPosition(self.random - self.gap)

    def move(self):
        if not self.stop:
            self.pipe0.move()
            self.pipe1.move()

    def delete(self):
        self.pipe0.kill()
        self.pipe1.kill()

    def blit(self):
        self.move()
        self.screen.blit(self.pipe0.image, self.pipe0.rect)
        self.screen.blit(self.pipe1.image, self.pipe1.rect)
