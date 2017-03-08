import pygame
class Board:
    def __init__(self,screen):
        self.screen = screen
        print("Hello")
        
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
    
    
    
