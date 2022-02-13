from turtle import color
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

#Generic Ship class to be inherited by both player and enemy ships
class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    #Method to draw instance to window
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

class Enemy(Ship):
    #Used for when color strings are passed to define mapping for ship and laser colors 
    COLOR_MAP = {
                "red": (RED_SPACE_SHIP, RED_LASER),
                "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
                }
    
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel



def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    
    #Ship velocity
    player_vel = 5

    #Instanciated instance of Ship class
    player = Player(300, 650)

    clock = pygame.time.Clock()

    def redraw_window():
        #Draw background to window
        WIN.blit(BG, (0,0))

        #Draw Text to window
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        #Using non-hard coded values allows for window resizing while maintaining render placements
        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        #Method used to draw instance of player to window
        player.draw(WIN)

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
        
        #Checks based on fps what keys are pressed and returns bool values with True if they are pressed
        keys = pygame.key.get_pressed()
        #If statement for the key at this index (.K represents keyboard input and _value equals which key)
        if keys[pygame.K_a] and player.x - player_vel > 0: #Left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: #Right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0: #Up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT: #Down
            player.y += player_vel

main()
