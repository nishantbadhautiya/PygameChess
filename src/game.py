import pygame 
from const import * 
from board import Board 
from square import Square 
from piece import Piece

class Game: 
    def __init__(self) -> None:
        self.board = Board() 

    # show methods 
    def show_bg(self, surface):
        for row in range(ROWS): 
            for col in range(COLS):
                if (row + col) % 2 == 0: 
                    color = (234, 235, 200) # Light Gray 
                else: 
                    color = (119, 154, 88) # Dark Green 

                rectange = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface=surface, color=color, rect= rectange)

    def show_pieces(self, surface): 
        for row in range(ROWS): 
            for col in range(COLS):
                # piece ? 
                if self.board.squares[row][col].has_piece(): 
                    piece = self.board.squares[row][col].piece 
                    img = pygame.image.load(piece.texture)
                    img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                    piece.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)