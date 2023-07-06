import pygame as pg
import os
from settings import *
from bird import *
from score import *
from pipes import *

#TODO: fix rotation when flapping
#TODO: implement pipes
#TODO: implement score
#TODO: make background move

class Game():
    def __init__(self):
        pg.init()
        pg.font.init()
        pg.display.set_caption("Flappy Bird")
        pg.display.set_icon(pg.image.load(os.path.join("OneDrive", "Desktop", "flappy_bird_game", "assets", "bird", "Bird_0.png")))
        
        self.background = pg.transform.scale(pg.image.load(os.path.join("OneDrive", "Desktop", "flappy_bird_game", "assets", "Background.jpg")), (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.clock = pg.time.Clock()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()
                if event.key == pg.K_SPACE:
                    bird.move()
    
    def draw_window(self):
        SCREEN.blit(self.background, (0,0))
        bird.update()
        if bird.active:
            upper_pipe.update()
            downer_pipe.update()

    def update(self):
        pg.display.update()
        self.clock.tick(FPS)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw_window()

game = Game()
game.run()