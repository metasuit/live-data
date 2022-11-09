# ---
# Game Template
# ---

import pygame, sys, random

# General Setup
pygame.init()
clock = pygame.time.Clock()  # Limit fps

# Game variables
game_active = True

# Game Screen
screen_width = 500
screen_height = 500
pygame.display.set_caption("Playground X")
screen = pygame.display.set_mode((screen_width, screen_height))  # Image canvas


while True:  # Game loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                # Action goes here
                print(' ')
            if event.key == pygame.K_SPACE and not game_active:
                game_active == True

    pygame.display.update()  #Draws everything on the screen, what has been drawn before
    clock.tick(60)  # Can't run faster than 60 fps
