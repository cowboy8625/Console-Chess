from os import system, name
from time import sleep
from colorama import Fore, init

init(autoreset=True)


def clear():
    system("cls" if name == "nt" else "clear")


def piece_switch(p):
    return {
        "WK": chr(9812),
        "WQ": chr(9813),
        "WR": chr(9814),
        "WB": chr(9815),
        "WN": chr(9816),
        "WP": chr(9817),
        "BK": chr(9818),
        "BQ": chr(9819),
        "BR": chr(9820),
        "BB": chr(9821),
        "BN": chr(9822),
        "BP": chr(9823),
    }.get(p, None)


def col_switch(col):
    return {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}.get(
        col, None
    )


def transform(loc):
    y, x = loc
    return int(x), (col_switch(y) * 2)


class Board:
    def __init__(self, width, height):
        self.board = [
            [" " for _ in range(int(width))]
            if h % 2 == 0
            else ["-" for _ in range(int(width))]
            for h in range(height * 2)
        ][0:-1]

    def build(self, w, h):
        for p in w:
            self.board[p.col][p.row] = p

        for p in h:
            self.board[p.col][p.row] = p

    def clear(self):
        for line in self.board:
            line.clear()

    def render(self):
        result = []
        for i, t in enumerate(self.board):
            if i % 2 == 0:
                result.append(
                    " |".join([i.name if isinstance(i, Piece) else i for i in t])
                )
            else:
                t[-1] = "--"
                result.append("-|".join(t))
        clear()
        print("\n".join(result))

    def move(self, _from, _to):
        piece = self.get_piece(_from)
        piece.move(_to)
        self.place(piece)
        self.erase(_from)

    def get_piece(self, loc):
        x, y = transform(loc)
        print(x, y)
        p = self.board[y][x]
        return p

    def place(self, p):
        self.board[p.col][p.row] = p

    def erase(self, loc):
        x, y = transform(loc)
        self.board[y][x] = " "


class Piece:
    def __init__(self, name, loc):
        self.name = piece_switch(name)
        self.row, self.col = transform(loc)

    def __repr__(self):
        return f"Piece({self.name}, {self.row}, {self.col})"

    def __str__(self):
        return f"{self.name}"

    def move(self, loc):
        self.row, self.col = transform(loc)


board = Board(width=8, height=8)

white = [
    Piece("WR", "A0"),
    Piece("WN", "A1"),
    Piece("WB", "A2"),
    Piece("WK", "A3"),
    Piece("WQ", "A4"),
    Piece("WB", "A5"),
    Piece("WN", "A6"),
    Piece("WR", "A7"),
    Piece("WP", "B0"),
    Piece("WP", "B1"),
    Piece("WP", "B2"),
    Piece("WP", "B3"),
    Piece("WP", "B4"),
    Piece("WP", "B5"),
    Piece("WP", "B6"),
    Piece("WP", "B7"),
]
black = [
    Piece("BR", "H0"),
    Piece("BN", "H1"),
    Piece("BB", "H2"),
    Piece("BQ", "H3"),
    Piece("BK", "H4"),
    Piece("BB", "H5"),
    Piece("BN", "H6"),
    Piece("BR", "H7"),
    Piece("BP", "G0"),
    Piece("BP", "G1"),
    Piece("BP", "G2"),
    Piece("BP", "G3"),
    Piece("BP", "G4"),
    Piece("BP", "G5"),
    Piece("BP", "G6"),
    Piece("BP", "G7"),
]


board.build(white, black)


while True:
    board.render()
    loc = input("You Move:> ")
    _from, _to = loc.split(" ")
    board.move(_from, _to)

