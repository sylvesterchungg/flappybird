import pygame

class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = 60
        self.gap = 170
        self.top_height = 200
        self.speed = 3

    def draw(self, screen):
    # Top pipe
        pygame.draw.rect(
            screen,
            (0, 200, 0),
            (self.x, 0, self.width, self.top_height)
        )
        # Bottom pipe
        bottom_y = self.top_height + self.gap
        pygame.draw.rect(
            screen,
            (0, 200, 0),
            (self.x, bottom_y, self.width, 600 - bottom_y)
        )

    def update(self):
        self.x -= self.speed