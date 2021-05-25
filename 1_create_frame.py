import pygame

pygame.init() # init

# set screen size
screen_width = 480 # width
screen_height = 640 # height
screen = pygame.display.set_mode((screen_width, screen_height))

# my game title
pygame.display.set_caption("GAME")

# event loop
running = True # is it running?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# pygame end
pygame.quit()