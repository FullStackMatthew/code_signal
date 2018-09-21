import itertools
def sudoku(grid):
    #check if row is unique
    for r in grid:
        if len(set(r)) != 9: return False
    #check if column is unique
    for c in zip(*grid):
        if len(set(c)) != 9: return False
    #check if grid is unique
    g = []
    for r,c in itertools.product(range(3), repeat=2):
        g.append([grid[r+i][c+j] for i,j in itertools.product(range(0, 9, 3), repeat=2)])
    for c in zip(*g):
        if len(set(c)) != 9: return False
    return True