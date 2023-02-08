#!/usr/bin/env python3
import pygame, sys
from const import *
from game import Game
from piece import *
from play import *


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess")
        self.game = Game()



    def loop(self, mode, player_1 = None, player_2 = None):
        screen, game, dragger = self.screen, self.game, self.game.dragger
        run = True
        while run:
            game.show_background(screen)
            game.show_moves(screen)
            game.show_pieces(screen)

            if mode == 'H':
            
                if dragger.active:
                    dragger.update_blit(screen)

                for event in pygame.event.get():

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        
                        dragger.update_mouse(event.pos)
                        c_row = dragger.mouseY // SQ_SIZE
                        c_col = dragger.mouseX // SQ_SIZE
                        pos = (c_row,c_col)

                        if game.board.has_piece(pos) :
                            piece = game.board.get_piece(pos)
                            b = game.board
                            if piece.color == c_b[b.board.turn]:
                                
                                dragger.save_init(event.pos)
                                dragger.drag_piece(piece)

                                # moves 
                                game.show_background(screen)
                                game.show_pieces(screen)

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
                
            elif mode == 'E':
                # pygame.display.update()
                board = self.game.board

                if not board.board.is_game_over():
            
                    if player_1.is_turn():
                        player_1.engine_move()
                        # player_1.rand_player_move()
                        pygame.display.update()

                    else:
                        player_2.engine_move_()
                        pygame.display.update()

                else:

                    res = board.board.outcome().result()
                    status = board.board.outcome().termination
                    winner = {True:"WHITE",False:"BLACK"}[board.board.outcome().winner]

                    print(f"Result: {res} Status: {status} Winner: {winner}")
                    print("GAME OVER")
                    run = False
                    pygame.quit()
                    sys.exit()





            pygame.display.update()

        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                sys.exit()
        pygame.quit()






if __name__ == '__main__':


    mode = "E"
    

    if mode == "H":
        Main().loop(mode)
    else:
        m = Main()
        board = m.game.board

        player_1 = Player(board, 'w', True)
        player_2 = Player(board, 'b',True)
        m.loop(mode, player_1, player_2)

