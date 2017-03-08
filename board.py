import pygame
class Board:
    """Defines game board to be used for tic-tac-toe"""
    # Defines tiles on game board:
    """
    1 | 2 | 3
    __________
    4 | 5 | 6
    __________
    7 | 8 | 9
    """
    # Each tile is a list going from top-left -> top-right - > bottom-left -> 
    # bottom-right
    
    tile1 = [(0,100),(100,100),(0,200),(100,200)]
    tile2 = [(100,100),(200,100),(100,200),(200,200)]
    tile3 = [(200,100),(300,100),(200,200),(300,200)]
    tile4 = [(0,200),(100,200),(0,300),(100,300)]
    tile5 = [(100,200),(200,200),(100,300),(200,300)]
    tile6 = [(200,200),(300,200),(200,300),(300,300)]
    tile7 = [(0,300),(100,300),(0,400),(100,400)]
    tile8 = [(100,300),(200,300),(100,400),(200,400)]
    tile9 = [(200,300),(300,300),(200,400),(400,400)]
    
    # Create a list of all tiles
    tiles = (tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9)
    
    def __init__(self,screen):
        self.screen = screen
        print("Hello")

    def define_tile(self,top-left,top-right,bottom-right,bottom-left):
        topLeft = top-left
        topRight = top-right
        bottomLeft = bottom-left
        bottomRight = bottom-right
        center = ((topRight[0] - topLeft[0])/2, (topLeft[1] - bottomLeft[1])/2)
        
    def drawBoard(self):
    # function draws board made up of 4 lines to screen

    # Define characteristics of board such as line colour, thickness and line
    # coordinates

        BLACK = (0,0,0)
        THICKNESS = 2
        line1 = [(100,100),(100,400)]
        line2 = [(200, 100),(200,400)]
        line3 = [(0,200),(300,200)]
        line4 = [(0,300),(300,300)]
        linex1 = [(0,100),(100,200)]
        linex2 = [(100,100),(0,200)]

        # Draw the lines on the board
        pygame.draw.lines(self.screen,BLACK,False,line1,THICKNESS)
        pygame.draw.lines(self.screen,BLACK,False,line2,THICKNESS)
        pygame.draw.lines(self.screen,BLACK,False,line3,THICKNESS)
        pygame.draw.lines(self.screen,BLACK,False,line4,THICKNESS)
        pygame.draw.lines(self.screen,BLACK,False,linex1,THICKNESS)
        pygame.draw.lines(self.screen,BLACK,False,linex2,THICKNESS)
