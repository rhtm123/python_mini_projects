import pygame
from pygame.locals import *


if __name__ == "__main__":
    pygame.init()

    gameDisplay = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('A bit Racey')

    gameDisplay.fill((110, 110, 5))

    block_img = pygame.image.load("res/block.jpg")

    x, y = 100, 100

    gameDisplay.blit(block_img, (x, y))

    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_LEFT:
                    running = False
                if event.key == K_RIGHT:
                    running = False
                if event.key == K_UP:
                    running = False
                if event.key == K_DOWN:
                    running = False

            elif event.type == QUIT:
                running = False
