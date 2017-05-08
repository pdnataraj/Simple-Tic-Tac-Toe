import pygame
import sys
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (200,0,0)
BRIGHT_RED = (255,0,0)
GREEN = (0,200,0)
BRIGHT_GREEN = (0,255,0)
LIGHT_BLUE = (255,255,200)
display_width = 640
display_height = 480

def intro(screen,exit_game):
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
        
        screen.fill(WHITE)
    #-------------------------------------------------------------------------------    
        intro_text_font = pygame.font.SysFont('menlo',30)
        text = "A Simple Game of Tic-Tac-Toe"
        intro_text_surf = intro_text_font.render(text,True,BLACK)
        dest = (50,(display_height/2)-20)
        screen.blit(intro_text_surf,dest)
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        start_box = (100,300,100,50)
        quit_box = (500,300,100,50)
        
        if (100+100 > mouse[0] > 100 and 300+50 > mouse[1] > 300):
            pygame.draw.rect(screen, BRIGHT_GREEN,start_box)
            if (click[0] == 1):
                return
        else:
            pygame.draw.rect(screen, GREEN,start_box)
        
        if (500+100 > mouse[0] > 500 and 300+50 > mouse[1] > 300):
            pygame.draw.rect(screen, BRIGHT_RED,quit_box)
            if (click[0] == 1):
                exit_game = True
        else:
            pygame.draw.rect(screen, RED,quit_box) 
            
        button_text_font = pygame.font.SysFont('menlo',30)
        text = "Start"
        start_text_surf = button_text_font.render(text,True,BLACK)
        dest = pygame.Rect(start_box)
        screen.blit(start_text_surf,dest)
        
        button_text_font = pygame.font.SysFont('menlo',30)
        text = "Quit"
        quit_text_surf = button_text_font.render(text,True,BLACK)
        dest = pygame.Rect(quit_box)
        screen.blit(quit_text_surf,dest)     
    #-------------------------------------------------------------------------------  
        
        pygame.display.flip()
        # --- Limit to 60 frames per second
        clock.tick(60)    
    
    pygame.quit()
    quit()

def play_game(screen,exit_game):    
    import board
    clock = pygame.time.Clock()
    game_board = board.Board(screen)
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        screen.fill(WHITE)
        #-------------------------------------------------------------------------------
        game_board.drawBoard()
        mouse = pygame.mouse.get_pos()
        tile1 = (0,100,100,100)
        if (0+100 > mouse[0] > 0 and 100+50 > mouse[1] > 100):
            pygame.draw.rect(screen, LIGHT_BLUE,tile1)
        else:
            pygame.draw.rect(screen, WHITE,tile1)        
    #-------------------------------------------------------------------------------  
        
        pygame.display.flip()
        # --- Limit to 60 frames per second
        clock.tick(60)    
        
    return
    
    
    

    