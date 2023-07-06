import pygame as pg
import os
import math
from settings import *

class Background():
    def __init__(self):
        self.image = pg.transform.scale(pg.image.load(os.path.join("OneDrive", "Desktop", "flappy_bird_game", "assets", "Background.jpg")), (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.tile = math.ceil(SCREEN_WIDTH / self.image.get_width()) + 1
        self.scroll = 0

    def move(self):
        for i in range(0, self.tile):
            SCREEN.blit(self.image, (i * self.image.get_width() + self.scroll, 0))

        self.scroll -= BACKGROUND_SPEED

        if abs(self.scroll) > self.image.get_width():
            self.scroll = 0

    def update(self):
        self.move()

background = Background()