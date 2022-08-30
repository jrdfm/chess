import pygame, chess
from const import *
from board import Board
from piece import *


class Game(object):
    def __init__(self):
        self.board = Board()


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
        for row in range(ROWS):
            for col in range(COLS):
                loc = (row,col)
                if self.board.has_piece(loc):
                    name = self.board.get_color(loc)
                    color = self.board.get_name(loc)
                    piece = Piece(name, color)
                    img = pygame.image.load(piece.tex)
                    img_cen = col * SQ_SIZE + SQ_SIZE // 2, row * SQ_SIZE + SQ_SIZE // 2
                    piece.tex_rect = img.get_rect(center = img_cen)
                    surface.blit(img, piece.tex_rect)