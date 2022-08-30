from turtle import Screen
import pygame, sys
from const import *
from game import Game


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess")
        self.game = Game()

    def loop(self):
        screen, game = self.screen, self.game 
        while True:
            game.show_background(screen)
            game.show_pieces(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()


if __name__ == '__main__':
    Main().loop()