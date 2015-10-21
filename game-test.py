"""
 Base template from
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GROD = ( 218, 165,  32) 
FGREEN = (34,139,34)
SBROWN = (244,164,96)
BWOOD = (222,184,135)
CHIFFON = (255,250,205)
SBLUE = (176,196,222)
ORANGE = (204,102,0)
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
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
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    
    # Draw a rectangle
    pygame.draw.rect(screen,ORANGE,[20,20,655,100],0) 
    pygame.draw.rect(screen,ORANGE,[20,40,50,400],0)
    pygame.draw.rect(screen,ORANGE,[625,40,50,400],0)
    pygame.draw.rect(screen,ORANGE,[20,400,655,50],0)
    pygame.draw.rect(screen,CHIFFON,[70,120,560,280],0)
    
    # Draw on the screen several lines from (0,10) to (100,110)
    # 5 pixels wide using a for loop
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen,BLACK,[674,20+y_offset],[20,20+y_offset],2)   
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()