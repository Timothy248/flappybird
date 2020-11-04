import player as p
import pipePair as pipe
import replayButton as rb
import pygame
import variables as v

pygame.init()

screen = pygame.display.set_mode(v.gameSize)
title = pygame.display.set_caption("Flappy Bird")
backgroundImage = pygame.image.load("background.png")


clock = pygame.time.Clock()

player = p.Player()
player.rect.move_ip(v.gameSize[0] / 8, v.gameSize[1] / 3)

i = 0

ticker = 0
ticker1 = 0
pairs = [pipe.PipePair(200, screen)]
pairs1 = [pipe.PipePair(675, screen)]

dead = False


def collide(x, y):
    return pygame.sprite.collide_rect(x, y)


def checkForCollision():
    if collide(pairs[0].pipe0, player) or collide(pairs[0].pipe1, player):
        return True
    elif collide(pairs1[0].pipe0, player) or collide(pairs1[0].pipe1, player):
        return True
    else:
        return False


while True:
    clock.tick(v.fps)
    if pairs[ticker].pipe0.rect.centerx < -80:
        pairs[ticker].delete()
        pairs.append(pipe.PipePair(200, screen))
        pairs.pop(0)

    if pairs1[ticker1].pipe0.rect.centerx < -80:
        pairs1[ticker1].delete()
        pairs1.append(pipe.PipePair(200, screen))
        pairs1.pop(0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.flap()

    player.update()

    screen.blit(backgroundImage, [0, 0])

    pairs[ticker].blit()
    pairs1[ticker1].blit()

    screen.blit(player.image, player.rect)

    pygame.display.update()

    if checkForCollision() and not dead:
        dead = True
        pairs[0].stop = True
        pairs1[0].stop = True
        player.die()
