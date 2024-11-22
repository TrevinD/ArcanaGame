import pygame, os
from states.state import State

class Game_World(State):
    def __init__(self, game):
        State.__init__(self, game)

    def update(self, actions):
        pass

    def render(self, display):
        display.fill((204, 255, 229))