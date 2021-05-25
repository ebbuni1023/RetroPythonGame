import pygame

pygame.init() # init

# set screen size
screen_width = 480 # width
screen_height = 640 # height
screen = pygame.display.set_mode((screen_width, screen_height))

# my game title
pygame.display.set_caption("GAME")

# background
# background = pygame.image.load("C:\\Users\\ebbun\\Desktop\\GitHub\\RetroPythonGame\\background.png")

# event loop
running = True # is it running?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # game off

    screen.fill((55, 119, 132)) #background color
    # screen.blit(background, (0, 0)) # draw background

    pygame.display.update() # draw background again

# pygame end
pygame.quit()