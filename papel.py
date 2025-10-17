import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("One Papel Picado Banner")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)  
RED = (255, 0, 0)
GREEN = (80, 200, 20)
BLUE = (20, 120, 200)
ORANGE = (255, 140, 0)
YELLOW = (255, 255, 0)

bannerr = random.randint(0,255)
bannerg = random.randint(0,255)
bannerb = random.randint(0,255)

BANNER = (bannerr, bannerg, bannerb)


star = pygame.image.load('star.jpg')
width2 = 315
height2 = 180

scaled_size = (width2, height2)

small_star = pygame.transform.scale(star, scaled_size)




# Starting settings
current_color = RED
current_shape = "triangle"
SHAPE_SIZE = 40

# List of shapes (each shape is: [x, y, size, color, type])
shapeList = [] #this is going to be a LIST of LISTS!

# Initialize font for instructions
font = pygame.font.Font(None, 36)


# Main game loop-------------------------------------------------------------------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key presses
        elif event.type == pygame.KEYDOWN:
            
            #numbers select what shape to draw
            if event.key == pygame.K_1:
                current_shape = "ellipse"  # Select ellipse
            elif event.key == pygame.K_2:
                current_shape = "hexagon"  # Select hexagon
            elif event.key == pygame.K_3:
                current_shape = "triangle"  # Select triangle
            elif event.key == pygame.K_4:
                current_shape = "square"  # Select square
            elif event.key == pygame.K_5:
                current_shape = "circle"  # Select circle
            elif event.key == pygame.K_s:
                current_shape = "star"  # Change to star
            
            
            #letters select what color to draw with
            if event.key == pygame.K_r:
                current_color = RED  # Change to red
            elif event.key == pygame.K_g:
                current_color = GREEN  # Change to green
            elif event.key == pygame.K_b:
                current_color = BROWN  # Change to brown
            elif event.key == pygame.K_a:
                current_color = BLUE  # Change to blue
            elif event.key == pygame.K_o:
                current_color = ORANGE  # Change to orange
            elif event.key == pygame.K_y:
                current_color = YELLOW # Change to yellow
            elif event.key == pygame.K_d:
                current_color = BLACK  # Change to black
            elif event.key == pygame.K_w:
                current_color = WHITE  # Change to white

        # Check for mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            new_shape = [mouse_x, mouse_y, SHAPE_SIZE, current_color, current_shape]
            shapeList.append(new_shape)  # Add new shape to the list

    # Clear the screen
    screen.fill(WHITE)


    # draw one big banner rectangle
    pygame.draw.rect(screen, BANNER, (50, 50, 1100, 750 ))
        
    
    # Draw all shapes directly in the loop
    for i in range(len(shapeList)):
        x = shapeList[i][0]
        y = shapeList[i][1]
        size = shapeList[i][2]
        color = shapeList[i][3]
        kind = shapeList[i][4]

        if kind == "ellipse":
            pygame.draw.ellipse(screen, color, (x - size, y - size // 2, size * 2, size))  # Ellipse dimensions
        elif kind == "hexagon":
            points = [
                (x, y - size),  # Top
                (x + size, y - size // 2),  # Top-right
                (x + size, y + size // 2),  # Bottom-right
                (x, y + size),  # Bottom
                (x - size, y + size // 2),  # Bottom-left
                (x - size, y - size // 2)   # Top-left
            ]
            pygame.draw.polygon(screen, color, points)
        elif kind == "triangle":
            points = [
                (x, y - size),           # Top point
                (x - size, y + size),    # Bottom-left point
                (x + size, y + size)     # Bottom-right point
            ]
            pygame.draw.polygon(screen, color, points)
            
        elif kind == "square":
            points = [ 
                (x + size, y - size // 2),  # Top-right
                (x + size, y + size // 2),  # Bottom-right
                (x - size, y + size // 2),  # Bottom-left
                (x - size, y - size // 2)   # Top-left
            ]
            pygame.draw.polygon(screen, color, points)
        elif kind == "circle":
            points = [  
           
            ]
        elif kind == "star":
            points = [
                 screen.blit(small_star, (x, y))
                
                ]

    # Display instructions at the top
    instructions = font.render("1: Ellipse  2: Hexagon  3: Triangle 4: rectangle |  R: Red  G: Green  B: Brown Y: Yellow A: Blue ", True, BLACK)
    screen.blit(instructions, (10, 10))
    instructions = font.render("s:Star                                                                    |  O: Orange W: white", True, BLACK)
    screen.blit(instructions, (10, 35))

    # Update the screen
    pygame.display.flip()

pygame.quit()
