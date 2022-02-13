import pygame
import os
import time
import random
pygame.font.init()


WIDTH, HEIGHT = 750,750
#Considered a pygame surface that we can draw on.
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader Twist")

#Load images
#Enemy Ships
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

#Player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

#Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

#Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)

    clock = pygame.time.Clock()

    def redraw_window():
        #Draw background to window
        WIN.blit(BG, (0,0))

        #Draw Text to window
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        #Refreshes the display.
        pygame.display.update()

    while run:
        #Tick the clock based on FPS. Allows consistency on multiple devices.
        clock.tick(FPS)
        redraw_window()

        #Everytime we run the loop (60 times each second) loop through all events and
        #Check if an event occurs. If so do something.
        for event in pygame.event.get():
            #If you click the X in the pygame window run equals False
            if event.type == pygame.QUIT:
                run = False

main()
