# Screen dimensions
WIDTH = 600
HEIGHT = 600

# Board dimensions
ROWS = 8
COLS = 8
SQ_SIZE = WIDTH // COLS

BROWN, LIGHT_BROWN = (235, 209, 166), (165, 117, 80)

c = [(i,j) for i in range(7,-1,-1) for j in range(0,8)]
b  = [i for i in range(0,64)]

# car coordinate : board tile # dict 
c_to_b = dict(zip(c, b))
# type: name dict
t_n = {1:'P', 2:'K', 3:'B', 4:'R', 5:'Q', 6:'K'}
# color dict
c_b = {True: 'w', False: 'b'}