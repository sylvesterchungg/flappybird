import pygame 
import random

#Pygame setup
pygame.init()

WIDTH = 500
HEIGHT =  490

#Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

#define game var
flying = False
game_over = False
pipe_gap = 180
pipe_frequency = 1500 #ms
last_pipe = pygame.time.get_ticks() - pipe_frequency

##load images
bg = pygame.image.load('img/bg.png')

#Game loop control
running = True
#Create a clock object to control the frame rate
clock = pygame.time.Clock()

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1,4):
            img = pygame.image.load(f'img/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.velocity = 0

    def update(self):
        if flying == True:
            #gravity
            self.velocity += 0.5
            if self.velocity >= 7.5:
                self.velocity = 7.5
            if self.rect.bottom < 490:
                self.rect.y += int(self.velocity)
        if game_over == False:
            #Handle the animation
            self.counter += 1
            flap_cooldown = 5

            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]

            #rotation
            self.image = pygame.transform.rotate(self.images[self.index], self.velocity * -3)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)
            
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/pipe.png')
        self.image = pygame.transform.scale(img, (80, 380))
        self.rect = self.image.get_rect()
        #position 1 is from top where -1 is from bottom
        if position == -1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
        if position == 1:
            self.rect.topleft = [x,y + int(pipe_gap / 2)]

    def update(self):
        self.rect.x -= 5
        


bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

flappy = Bird(100, int(HEIGHT / 2))

bird_group.add(flappy)


#Game loop
while running:
    #Set the frame rate to 60 frames per second
    clock.tick(60)

    #Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            if not flying:
                flying = True
            flappy.velocity = -10

    screen.blit(bg,(0,0))   

    bird_group.draw(screen)
    bird_group.update()
    pipe_group.draw(screen)
    
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
        game_over = True

    #check if bird hit the ground
    if flappy.rect.bottom >= 490:
        game_over = True
        flying = False

    if not game_over and flying:
        #generate pipe
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, 100)
            btm_pipe = Pipe(WIDTH, int(HEIGHT / 2) + pipe_height, 1)
            top_pipe = Pipe(WIDTH, int(HEIGHT / 2) + pipe_height, -1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now

        pipe_group.update()


    #Update the display
    pygame.display.update()

#Close Program
pygame.quit()