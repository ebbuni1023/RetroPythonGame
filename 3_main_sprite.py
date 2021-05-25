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

# Call Sprite(character)
character = pygame.image.load("C:\\Users\\ebbun\\Desktop\\GitHub\\RetroPythonGame\\character.png")
character_size = character.get_rect().size # get size of image
character_width = character_size[0] # width of character 
character_height = character_size[1] # height of character
character_x_pos = (screen_width / 2) - (character_width / 2)# position half of width's size
character_y_pos = screen_height - character_height# position bottom of height

# event loop
running = True # is it running?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # game off

    screen.fill((55, 119, 132)) #background color
    # screen.blit(background, (0, 0)) # draw background
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() # draw background again

# pygame end
pygame.quit()