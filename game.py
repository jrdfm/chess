import pygame, chess
from const import *
from board import Board
from piece import *
from dragger import *


class Game(object):
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()


    def show_background(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2  == 0:
                    color = BROWN
                else:
                    color = LIGHT_BROWN

                rect = (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        board, dragger = self.board, self.dragger
        for row in range(ROWS):
            for col in range(COLS):
                pos = (row,col)
                if board.has_piece(pos):
                    piece = board.b[row][col] 
                    if piece is not dragger.piece:
                        piece.set_tex(size = 80)
                        img = pygame.image.load(piece.tex)
                        img_cen = col * SQ_SIZE + SQ_SIZE // 2, row * SQ_SIZE + SQ_SIZE // 2
                        piece.tex_rect = img.get_rect(center = img_cen)
                        surface.blit(img, piece.tex_rect)

    def show_moves(self, surface):
        dragger = self.dragger
        if dragger.active:
            piece = dragger.piece

            for move in piece.valid_moves:
                color = 
