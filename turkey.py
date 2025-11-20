import pygame
pygame.init()

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("November Holiday Turkey")
clock = pygame.time.Clock()

# background color
BG = (255,255,255)

title_font = pygame.font.SysFont(None, 38)


def draw_turkey(x, y):

    # --------------------------
    # TOP TEXT (unchanged)
    # --------------------------
    title1 = title_font.render("turkey independence day yayyayayay!!!", True, (0,0,0))
    screen.blit(title1, (80, 20))
 
    # --------------------------
    # FEATHER COLORS 
    # --------------------------
    RED        = (210, 0, 0)
    ORANGE     = (230, 140, 30)

    # --------------------------
    # FEATHERS (circle fan)
    # --------------------------
    pygame.draw.circle(screen, RED,       (x,      y - 120), 55)
    pygame.draw.circle(screen, ORANGE,    (x - 70, y - 90),  55)
    pygame.draw.circle(screen, ORANGE,    (x + 70, y - 90),  55)
    pygame.draw.circle(screen, RED,    (x - 110, y - 40),  55)
    pygame.draw.circle(screen, RED,    (x + 110, y - 40),  55)
    pygame.draw.circle(screen, ORANGE,    (x - 90, y + 5),  55)
    pygame.draw.circle(screen, ORANGE,    (x + 90, y + 5),  55)

    # --------------------------
    # BODY + HEAD
    # --------------------------
    pygame.draw.circle(screen, (71, 48, 6), (x, y - 20), 100)
    pygame.draw.circle(screen, (139, 69, 19), (x, y), 70)
    pygame.draw.circle(screen, (160, 82, 45), (x, y - 80), 40)
    pygame.draw.circle(screen, (71, 48, 6), (x, y + 10), 50)
   

    # --------------------------
    # EYES
    # --------------------------
    pygame.draw.circle(screen, (255, 255, 255), (x - 12, y - 92), 12)
    pygame.draw.circle(screen, (255, 255, 255), (x + 13, y - 92), 12)
    pygame.draw.circle(screen, (0, 0, 0), (x + 12, y - 92), 5)
    pygame.draw.circle(screen, (0, 0, 0), (x - 12, y - 92), 5)
    

    # --------------------------
    # BEAK + WATTLE
    # --------------------------
    pygame.draw.polygon(screen, ORANGE, [
        (x,      y - 50),
        (x - 12, y - 70),
        (x + 12, y - 70)
    ])
    pygame.draw.polygon(screen, RED, [
        (x + 1,   y - 50), 
        (x + 11, y - 67), #HIGHEST
        (x +18, y - 45)
    ])

    # ADD WATTLE HERE!

    # --------------------------
    # LEGS
    # --------------------------
    pygame.draw.rect(screen, ORANGE, (x - 28, y + 65, 12, 60))
    pygame.draw.rect(screen, ORANGE, (x + 15, y + 65, 12, 60))


# --------------------------
# MAIN LOOP
# --------------------------
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # print mouse (x, y) whenever the mouse moves
        if event.type == pygame.MOUSEMOTION:
            print("Mouse position:", event.pos)

    screen.fill(BG)
    draw_turkey(300, 230)
    pygame.display.flip()

pygame.quit()
