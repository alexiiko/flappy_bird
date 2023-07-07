import pygame as pg
import os
from settings import *
from pipes import *
from score import *

class Bird():
    def __init__(self):
        self.width = 65
        self.heigth = 65
        
        self.images = [pg.transform.scale(pg.image.load(os.path.join("OneDrive", "Desktop", "flappy_bird_game", "assets", "bird", f"Bird_{i}.png")), (self.width, self.heigth)) for i in range(2)]
        self.index = 0

        self.image = self.images[self.index]
        self.falling_image = pg.transform.rotate(self.image, 290)

        self.rect = self.falling_image.get_rect(center = (SCREEN_WIDTH//5, SCREEN_HEIGHT//4))

        self.hitbox = pg.Rect(self.rect.centerx, self.rect.centery, 55, 55)

        self.falling = 0
        self.gravity = 0

        self.active = False

    def animate(self):
        self.index += 0.05
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[int(self.index)]

    def restart(self):
        self.hitbox.center = (SCREEN_WIDTH//6, SCREEN_HEIGHT//4)
        self.active = False
        score.score = 0
        score.surface = GAME_FONT.render(f"Score: {score.score}", False, "black")
        upper_pipe.rect.left = SCREEN_WIDTH
        downer_pipe.rect.left = SCREEN_WIDTH
        pg.time.wait(TIME_AFTER_DEATH)

    def move(self):
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
            self.hitbox.y += self.gravity + 0.5

    def collision(self):
        if self.hitbox.colliderect(upper_pipe.rect) or self.hitbox.colliderect(downer_pipe.rect): 
            self.restart()

    def border(self):
        if self.hitbox.bottom <= 0:
            self.restart()
        
        if self.hitbox.top >= SCREEN_HEIGHT:
            self.restart()

    def draw(self):
        SCREEN.blit(self.image, self.hitbox)

    def update(self):
        self.collision()
        self.animate()
        self.rotate()
        self.fall()
        self.border()
        self.draw()

bird = Bird()