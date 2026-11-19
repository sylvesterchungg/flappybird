import pygame

#Pygame setup
pygame.init()

WIDTH, HEIGHT = 400, 600

#Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#Title of the window
pygame.display.set_caption("Flappy Bird")

#Game loop control
running = True

#Create a clock object to control the frame rate
clock = pygame.time.Clock()

#Game loop
while running:
    #Set the frame rate to 60 frames per second
    clock.tick(60)

    #Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill the screen with a color (RGB)
    screen.fill((135, 206, 235))  # Sky blue color

    #Update the display
    pygame.display.flip()

#Close Program
pygame.quit()