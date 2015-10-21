"""
 Base template from
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
import pygame
import random
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
ORANGE = (254,196,79)
PERU = (205,133,63)
DORANGE = (217,95,14)
LORANGE = (255,247,188)
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
def draw_icon(screen, x, y):
    pygame.draw.ellipse(screen, BLACK, [1+x,y,10,10], 0) 
 
# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 300
y_coord = 300
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Hide the mouse cursor
pygame.mouse.set_visible(False)
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
            # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
             
                # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0 
    # --- Game logic should go here   

    # Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed
    
  
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    
    # Draw a rectangle
    pygame.draw.rect(screen,ORANGE,[20,20,655,100],0) 
    pygame.draw.rect(screen,ORANGE,[20,40,50,400],0)
    pygame.draw.rect(screen,ORANGE,[625,40,50,400],0)
    pygame.draw.rect(screen,ORANGE,[20,400,655,50],0)
    pygame.draw.rect(screen,LORANGE,[70,120,560,280],0)
    
    # Draw on the screen several lines from (0,10) to (100,110)
    # 5 pixels wide using a for loop
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen,DORANGE,[674,20+y_offset],[20,20+y_offset],2)  
    # Icon
    draw_icon(screen, x_coord, y_coord)        
 
    # --- Go ahead and update the screen with what we've drawn.

    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()