import pygame

import constants
from constants import *
from assets.asset_manager import *


# ui_elements.py (updated)
class Text():
    def __init__(self, text, font, size, color, x, y):
        self.text = text
        self.font = font
        self.size = size
        self.color = color
        self._rendered_text = None
        self._render_cache = {}  # Localized cache for this text element

    def render(self, screen):
        if self._rendered_text is None or (self.text, self.size, self.color) not in self._render_cache:
            self._rendered_text = self._render_text()
            self._render_cache[(self.text, self.size, self.color)] = self._rendered_text
        screen.blit(self._rendered_text, (self.x, self.y))

    def _render_text(self):
        asset_manager = AssetManager()
        return asset_manager.render_text(self.font, self.text, self.size, self.color)

class Button():
    #... (existing code, potentially using the new Text class)
    pass

class Label(Text):
    #... (existing code, potentially using the new Text class)
    pass

class TextInputBox:
    def __init__(self, x, y, width, height, initial_text='', font_size=FONT_SIZE,
                 on_confirm_callback=None, confirm_prompt="Is '{}' correct? (Y/N)"):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = initial_text
        self.active = True
        self.confirm_requested = False
        self.confirmed_text = ""
        self.font = constants.FONT_8_BIT_WONDER
        self.confirm_font = constants.FONT_8_BIT_WONDER
        self.on_confirm_callback = on_confirm_callback
        self.confirm_prompt = confirm_prompt

    def handle_event(self, event, game_instance):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.confirm_requested = True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

        if event.type == pygame.KEYDOWN and self.confirm_requested:
            if event.key == pygame.K_y:
                self.confirmed_text = self.text
                if self.on_confirm_callback:
                    self.on_confirm_callback(self.confirmed_text)
                self.confirm_requested = False
            elif event.key == pygame.K_n:
                self.confirm_requested = False

    def draw(self, screen):
        color = WHITE if self.active else (200, 200, 200)
        pygame.draw.rect(screen, color, self.rect, 2)
        text_surface = self.font.render(self.text, True, constants.BLACK)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

        if self.confirm_requested:
            confirm_text = self.confirm_font.render(self.confirm_prompt.format(self.text), True, BLACK)
            screen.blit(confirm_text, (self.rect.x, self.rect.y + self.rect.height + 10))

