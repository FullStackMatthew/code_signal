def chessKnight(cell):
    r = [2, 3, 4, 6, 8]
    c1 = min(ord(cell[0]) - 97, 104 - ord(cell[0]));
    c2 = min(ord(cell[1]) - 49, 56 - ord(cell[1]));
    d1 = min(c1, 2);
    d2 = min(c2, 2);
    return r[d1 + d2]