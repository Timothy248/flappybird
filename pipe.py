import pygame
import variables as v


class Pipe(pygame.sprite.Sprite):
    def __init__(self, isTop, startingPosition):
        super().__init__()
        self.isTop = isTop

        self.x = v.gameSize[0] + 100
        self.startingPosition = startingPosition

        if self.isTop:
            self.rect = pygame.Rect((0, 0), (104, 800))
            self.image = pygame.image.load("topPipe.png")

            self.y = self.image.get_rect().height * -1
        else:
            self.rect = pygame.Rect((0, 0), (104, 800))
            self.image = pygame.image.load("bottomPipe.png")

            self.y = self.image.get_rect().height

    def setPosition(self, y):
        if self.isTop:
            self.y += y
        else:
            self.y -= y

        self.rect.move_ip(v.gameSize[0] + self.startingPosition, self.y)

    def move(self):
        self.rect.move_ip(v.speed * -1, 0)


