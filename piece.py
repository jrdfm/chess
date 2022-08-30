import os

class Piece:
    def __init__(self, name, color, tex = None, tex_rect = None):
        self.name = name
        self.color = color
        self.tex = tex
        self.set_tex()
        self.tex_rect = tex_rect

    def set_tex(self):
        self.tex = os.path.join(f'img/{self.name}{self.color}.png')
       
    #    /home/jrdfm/fun/chess/chess_1.0/img

class Pawn(Piece):

    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1
        self.en_passant = False
        super().__init__('P', color)

class Knight(Piece):

    def __init__(self, color):
        super().__init__('N')

class Bishop(Piece):

    def __init__(self, color):
        super().__init__('B', color)

class Rook(Piece):

    def __init__(self, color):
        super().__init__('R', color)

class Queen(Piece):

    def __init__(self, color):
        super().__init__('Q', color)

class King(Piece):

    def __init__(self, color):
        self.left_rook = None
        self.right_rook = None
        super().__init__('king', color)



if __name__ == '__main__':

    import os 
    from PIL import Image
    p = Piece('b','Q')
    # print("ASS")
    # entries = os.listdir('img/')
    # for entry in entries:
    #     print(entry)
    img = os.path.join(f'img/{p.name}{p.color}.png')
    # cwd = os.getcwd()
    # print(cwd)
    # print(img)
    # print(os.path.abspath(img))
    # im = Image.open(os.path.abspath(img))
    im = Image.open(img)
    im.show()