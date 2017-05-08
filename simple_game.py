import game_sequences
import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (200,0,0)
BRIGHT_RED = (255,0,0)
GREEN = (0,200,0)
BRIGHT_GREEN = (0,255,0)


pygame.init()
pygame.font.init()  
# Set the width and height of the screen [width, height]
display_width = 640
display_height = 480
size = (display_width, display_height)
screen = pygame.display.set_mode(size)
exit_game = False

game_screen = game_sequences.intro(screen, exit_game)
exit_game = False
game_sequences.play_game(screen,exit_game)

