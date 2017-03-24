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
    
    BLACK = (0,0,0)
    THICKNESS = 2    
    
    # Create a tuple of all tiles
    tiles = (tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9)
    
    def __init__(self,screen):
        self.screen = screen
        print("Hello")
    
   
    def drawBoard(self):
    # function draws board made up of 4 lines to screen

    # Define characteristics of board such as line colour, Board.THICKNESS and line
    # coordinates

        line1 = [(100,100),(100,400)]
        line2 = [(200, 100),(200,400)]
        line3 = [(0,200),(300,200)]
        line4 = [(0,300),(300,300)]
        linex1 = [(0,100),(100,200)]
        linex2 = [(100,100),(0,200)]

        # Draw the lines on the board
        pygame.draw.lines(self.screen,Board.BLACK,False,line1,Board.THICKNESS)
        pygame.draw.lines(self.screen,Board.BLACK,False,line2,Board.THICKNESS)
        pygame.draw.lines(self.screen,Board.BLACK,False,line3,Board.THICKNESS)
        pygame.draw.lines(self.screen,Board.BLACK,False,line4,Board.THICKNESS)

    def draw_on_tile(self,tile_num):
        """"This method draws on the tile"""
        tile = self.tiles[tile_num-1]
        tile_line1 = (tile[0],tile[2])
        tile_line2 = (tile[1],tile[3])
        pygame.draw.lines(self.screen,Board.BLACK,False,tile_line1, Board.THICKNESS)
        pygame.draw.lines(self.screen,Board.BLACK,False,tile_line2, Board.THICKNESS)
        
        #elif(move == 'o' or move =='O'):
            #tile_center = (int((tile_topRight[0] - tile_topLeft[0])/2), int((tile_topLeft[1] - tile_botLeft[1])/2))
            #tile_radius = 100
            #pygame.draw.circle(self.screen,Board.BLACK,tile_center, tile_radius, 1)
        
        #else:
            #print("Enter either x,X,o or O")
             