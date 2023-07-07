import pygame as pg
import os
from random import randint
from settings import *

class UpperPipe():
    def __init__(self):
        self.image = pg.image.load(os.path.join("OneDrive", "Desktop", "flappy_bird_game", "assets", "Upper_Pipe.png"))
        self.rect = self.image.get_rect(midbottom = (SCREEN_WIDTH + self.image.get_width(), randint(10, self.image.get_height())))

    def move(self):
        self.rect.x -= PIPE_SPEED

    def reset_position(self):
        if self.rect.right <= 0:
            self.rect.left = SCREEN_WIDTH
            self.change_position()
            #self.get_faster()
            return True
        return False

    def get_faster(self):
        FPS += 2

    def change_position(self):
        self.rect.bottom = randint(10, self.image.get_height())
        return self.rect.bottom

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def update(self):
        self.reset_position()
        self.move()
        self.draw()

upper_pipe = UpperPipe()

class DownerPipe():
    def __init__(self):
        self.image = pg.image.load(os.path.join("OneDrive", "Desktop", "flappy_bird_game", "assets", "Downer_Pipe.png"))
        self.rect = self.image.get_rect(midtop = (SCREEN_WIDTH + self.image.get_width(), randint(SCREEN_HEIGHT- self.image.get_height(), SCREEN_HEIGHT)))

    def move(self):
        self.rect.x -= PIPE_SPEED

    def reset_position(self):
        if self.rect.right <= 0:
            self.rect.left = SCREEN_WIDTH
            #self.get_faster()
            self.change_position()
            return True
        return False

    def change_position(self):
        self.rect.top = randint(SCREEN_HEIGHT- self.image.get_height(), SCREEN_HEIGHT)
        
    def get_faster(self):
        FPS += 2

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def update(self):
        self.reset_position()
        self.move()
        self.draw()

downer_pipe = DownerPipe()