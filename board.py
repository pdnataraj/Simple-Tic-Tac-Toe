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
    # bottom-right corners. The fifth element will be the tile image
    # Each tile is 100x100 px wide and high
    board_tiles = {}
    tile1 = [(0,100),(100,100),(0,200),(100,200),"Images/one.png"]
    tile2 = [(100,100),(200,100),(100,200),(200,200),"Images/two.png"]
    tile3 = [(200,100),(300,100),(200,200),(300,200),"Images/three.png"]
    tile4 = [(0,200),(100,200),(0,300),(100,300),"Images/four.png"]
    tile5 = [(100,200),(200,200),(100,300),(200,300),"Images/five.png"]
    tile6 = [(200,200),(300,200),(200,300),(300,300),"Images/six.png"]
    tile7 = [(0,300),(100,300),(0,400),(100,400),"Images/seven.png"]
    tile8 = [(100,300),(200,300),(100,400),(200,400),"Images/eight.png"]
    tile9 = [(200,300),(300,300),(200,400),(400,400),"Images/nine.png"]
    
    # Create a list of all tiles
    tiles = [tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9]
    
    # Add tiles to a dictionary
    for i in range(1,10):
        board_tiles[i] = tiles[i-1]
    
    # Define colour and thickness
    BLACK = (0,0,0)
    THICKNESS = 2    
    
    # Constructor function
    def __init__(self,screen):
        self.screen = screen
    def drawBoard(self):
    # function draws board made up of 4 lines to screen

    # Define characteristics of board such as line colour, Board.THICKNESS and line
    # coordinates

        line1 = [(100,100),(100,400)]
        line2 = [(200, 100),(200,400)]
        line3 = [(0,200),(300,200)]
        line4 = [(0,300),(300,300)]

        # Draw the lines on the board
        pygame.draw.lines(self.screen,(0,0,0),False,line1,Board.THICKNESS)
        pygame.draw.lines(self.screen,(0,0,0),False,line2,Board.THICKNESS)
        pygame.draw.lines(self.screen,(0,0,0),False,line3,Board.THICKNESS)
        pygame.draw.lines(self.screen,(0,0,0),False,line4,Board.THICKNESS)


    
             