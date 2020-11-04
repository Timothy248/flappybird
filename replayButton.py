import pygame
import variables as v


class ReplayButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.size = v.replayButtonSize

        self.rect = pygame.Rect((v.gameSize[0] / 2, v.gameSize[1] / 2), self.size)
        self.image = pygame.Surface(self.size)
