import chess
# Screen dimensions
WIDTH = 600
HEIGHT = 600

# Board dimensions
ROWS = 8
COLS = 8
SQ_SIZE = WIDTH // COLS

BROWN, LIGHT_BROWN = (235, 209, 166), (165, 117, 80)
RED, LIGHT_RED = '#C86464', '#C84646'

c = [(i,j) for i in range(7,-1,-1) for j in range(0,8)]
b  = [i for i in range(0,64)]

# car coordinate : board tile # dict 
c_to_b = dict(zip(c, b))
b_to_c = dict(zip(b, c))
# type: name dict
t_n = {1:'P', 2:'N', 3:'B', 4:'R', 5:'Q', 6:'K'}
# color dict
c_b = {True: 'w', False: 'b'}

# values dict

val = {'p':-1,'n':-3,'b':-3,'k':0,'q':9,'r':5,'P':1,'N':3,'B':3,'K':0,'Q':9,'R':5}


if __name__ == '__main__':
    print(f'{c_to_b[(0,7)]}')