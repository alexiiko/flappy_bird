from settings import *
from pipes import *
from bird import *

class Score():
    def __init__(self):
        self.font = GAME_FONT
        self.score = 0
        self.surface = GAME_FONT.render(f"Score: {self.score}", False, "black")

    def increase_score(self):
        if upper_pipe.reset_position() or downer_pipe.reset_position():
            self.score += 1
            self.surface = GAME_FONT.render(f"Score: {self.score}", False, "black")

    def draw_score(self):
        SCREEN.blit(self.surface, (0,0))

    def update(self):
        self.increase_score()
        self.draw_score()

score = Score()