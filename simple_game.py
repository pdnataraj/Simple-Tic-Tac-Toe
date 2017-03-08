import pygame
import sys
#added this comment
from draw_board import Board
BLACK = (0,0,0)
WHITE = (255,255,255)
pygame.init()
pygame.font.init()
myFont = pygame.font.SysFont('Arial',30)
text = "Hello and Welcome to Paul's fantastic game!"
textSurface = myFont.render(text,False,BLACK)


# Set the width and height of the screen [width, height]
size = (640, 480)
screen = pygame.display.set_mode(size)
game_board = Board(screen)
pygame.display.set_caption("Paul's Cool Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    screen.blit(textSurface,(0,10))
    game_board.drawBoard() 
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
sys.exit()