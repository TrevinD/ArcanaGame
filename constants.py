# constants.py
import os

import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
FONT_SIZE = 20
ASSETS_DIR = os.path.join("Assets")
ART_DIR = os.path.join(ASSETS_DIR, "art")
FONT_DIR = os.path.join(ASSETS_DIR, "font")
FONT_8_BIT_WONDER = os.path.join(FONT_DIR, "8-BIT_WONDER.TTF")


# Screen and Game Canvas Dimensions
GAME_W, GAME_H = 480, 270
SCREEN_W, SCREEN_H = 960, 540