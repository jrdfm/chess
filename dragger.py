import pygame

from const import *

class Dragger:

    def __init__(self):
        self.mouseX = self.mouseY = 0
        self.init_row = 0
        self.init_col = 0
        self.piece = None
        self.active = False
    
    def update_mouse(self, pos):
        self.mouseX , self.mouseY = pos
    
    def update_blit(self, surface):
        self.piece.set_tex(size = 128)
        tex = self.piece.tex
        img = pygame.image.load(tex)
        img_cen = (self.mouseX, self.mouseY)
        self.piece.tex_rect = img.get_rect(center = img_cen)
        surface.blit(img, self.piece.tex_rect)

    def save_init(self, pos):

        self.init_row =  pos[1] // SQ_SIZE 
        self.init_col =  pos[0] // SQ_SIZE 

    def drag_piece(self, piece):
        self.piece = piece
        self.active = True
    def undrag_piece(self, piece):
        self.piece = None
        self.active = None