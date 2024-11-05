from const import * 
from square import Square 
from piece import *

class Board: 
    def __init__(self) -> None:
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self._create() 
        self._add_pieces(color='white') 
        self._add_pieces(color='black')  

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row= row, col= col)

    def _add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0) 
        # pawn
        for col in range(COLS): 
            self.squares[row_pawn][col] = Square(row=row_pawn, col=col, piece=Pawn(color=color))
        
        # rook 
        self.squares[row_other][0] = Square(row= row_other, col=0, piece=Rook(color= color)) 
        self.squares[row_other][7] = Square(row=row_other, col=7, piece= Rook(color= color)) 

        # knight 
        self.squares[row_other][1] = Square(row=row_other, col=1, piece=Knight(color= color)) 
        self.squares[row_other][6] = Square(row=row_other, col=6, piece=Knight(color= color)) 

        # bishop 
        self.squares[row_other][2] = Square(row=row_other, col=2, piece=Bishop(color= color)) 
        self.squares[row_other][5] = Square(row=row_other, col=5, piece=Bishop(color= color)) 

        # queen 
        self.squares[row_other][3] = Square(row=row_other, col=3, piece=Queen(color= color)) 

        # king 
        self.squares[row_other][4] = Square(row=row_other, col=4, piece=King(color= color)) 