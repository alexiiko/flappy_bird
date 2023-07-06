import pygame as pg
import os
from settings import *
from pipes import *

class Bird():
    def __init__(self):
        self.width = 75
        self.heigth = 75
        
        self.image = pg.transform.scale(pg.image.load(os.path.join("OneDrive", "Desktop", "flappy_bird_game", "assets", "Bird.png")), (self.width, self.heigth))
        self.falling_image = pg.transform.rotate(self.image, 290)
        self.flapping_image = pg.transform.rotate(self.image, 50)

        self.rect = self.falling_image.get_rect(center = (SCREEN_WIDTH//6, SCREEN_HEIGHT//4))

        self.falling = 0
        self.gravity = 0

        self.active = False

    def restart(self):
        pg.time.wait(1000)
        self.rect.center = (SCREEN_WIDTH//6, SCREEN_HEIGHT//4)

    def move(self):
        self.image = self.flapping_image
        self.gravity = -BIRD_JUMP_HEIGHT
        self.falling = 0
        self.active = True

    def rotate(self):
        if self.active:
            self.falling += 1

            if self.falling >= 25:
                self.image = self.falling_image

    def fall(self):
        if self.active:
            self.gravity += BIRD_FALL_SPEED
            self.rect.y += self.gravity

    def collision(self):
        pass

    def increase_score(self):
        pass

    def border(self):
        if self.rect.bottom <= 0:
            self.restart()

        if self.rect.top >= SCREEN_HEIGHT:
            self.restart()

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def update(self):
        self.rotate()
        self.fall()
        self.border()
        self.draw()

bird = Bird()