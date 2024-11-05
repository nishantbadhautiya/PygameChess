import pygame 
from const import * 

class Game: 
    def __init__(self) -> None:
        pass

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

                pygame.display.update() 

