import pygame as pg
import os
from settings import *

class UpperPipe():
    def __init__(self):
        self.image = pg.image.load(os.path.join("OneDrive", "Desktop", "flappy_bird_game", "assets", "Upper_Pipe.png"))
        self.rect = self.image.get_rect(midtop = (SCREEN_WIDTH + self.image.get_width(), 0))

    def move(self):
        self.rect.x -= PIPE_SPEED

    def reset_position(self):
        pass

    def get_faster(self):
        pass

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def update(self):
        self.move()
        self.draw()

upper_pipe = UpperPipe()

class DownerPipe():
    def __init__(self):
        self.image = pg.image.load(os.path.join("OneDrive", "Desktop", "flappy_bird_game", "assets", "Downer_Pipe.png"))
        self.rect = self.image.get_rect(midbottom = (SCREEN_WIDTH + self.image.get_width(), SCREEN_HEIGHT))

    def move(self):
        self.rect.x -= PIPE_SPEED

    def reset_position(self):
        pass

    def get_faster(self):
        pass

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def update(self):
        self.move()
        self.draw()

downer_pipe = DownerPipe()