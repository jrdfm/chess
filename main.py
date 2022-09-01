from turtle import Screen
import pygame, sys
from const import *
from game import Game
from piece import *


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess")
        self.game = Game()



    def loop(self):
        screen, game, dragger = self.screen, self.game, self.game.dragger
        run = True
        while run:
            game.show_background(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            
            if dragger.active:
                dragger.update_blit(screen)

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    dragger.update_mouse(event.pos)
                    c_row = dragger.mouseY // SQ_SIZE
                    c_col = dragger.mouseX // SQ_SIZE
                    pos = (c_row,c_col)

                    if game.board.has_piece(pos):
                        piece = game.board.get_piece(pos)
                        game.board
                        dragger.save_init(event.pos)
                        dragger.drag_piece(piece)

                        # moves 
                        game.show_background(screen)
                        # game.show_moves(screen)
                        game.show_pieces(screen)
                        print(f'{piece.valid_moves}')

                elif event.type == pygame.MOUSEMOTION:
                    if dragger.active:
                        dragger.update_mouse(event.pos)
                        dragger.update_blit(screen)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.active:
                        piece = dragger.piece
                        dragger.update_mouse(event.pos)
                        r_row = dragger.mouseY // SQ_SIZE
                        r_col = dragger.mouseX // SQ_SIZE
                        pos = (r_row,r_col)
                        ini = (dragger.init_row, dragger.init_col)
                        fin = (r_row, r_col )
                        move = (ini, fin)

                        if game.board.is_legal(move):
                            game.board.move(piece, move)
                            game.show_background(screen)
                            game.show_pieces(screen)

                        dragger.undrag_piece(piece)

                elif event.type == pygame.QUIT:
                    run = False

            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    Main().loop()