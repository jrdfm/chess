
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



    def loop(self, mode):
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
                player_1 = Player(board, 'w', True)
                player_2 = Player(board, 'b',True)
                if not board.board.is_game_over():
            
                    if player_1.is_turn():
                        player_1.engine_move()
                        pygame.display.update()

                    else:
                        player_2.engine_move()
                        pygame.display.update()

                else:
                    print("GAME IS OVER")
                    pygame.quit()

                # board = self.game.board.board
                # for event in pygame.event.get():
                #     p = Play(board)
                #     p.play()
                #     pygame.display.update()

                #     if event.type == pygame.QUIT:
                #         break


                #     elif event.type == pygame.USEREVENT:
                #         print(f'event')
                #         game.show_background(screen)
                #         game.show_pieces(screen)
                #         pygame.display.update()
                    

            pygame.display.update()
        pygame.quit()


# class Play:
#     def __init__(self, board):
#         self._board = board

#     def play(self):
#         player_1 = Player(self._board, 'w', True)
#         player_2 = Player(self._board, 'b',True)
#         board = self._board
#         move_event = pygame.event.Event(pygame.USEREVENT)
        
#         if not board.is_game_over():
            
#             if player_1.is_turn():
#                 board = player_1.engine_move()
#                 pygame.event.post(move_event)

#             else:
#                 board = player_2.engine_move()
#                 pygame.event.post(move_event)

#         else:
#             print("GAME IS OVER")
#             pygame.event.post(pygame.QUIT)


if __name__ == '__main__':


    mode = "E"
    

    if mode == "H":
        Main().loop(mode)
    else:
        m = Main()
        board = m.game.board
        m.loop(mode)
