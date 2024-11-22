import os.path
import os

import pygame, pygame_gui
from states.title import Title
from states.titlemenu import TitleMenu
from states.new_game import NewGame

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, True
        self.actions = {"left": False, "right": False, "up": False, "down": False, "back": False, "start": False}
        self.key_delay = 200  # Initial delay in milliseconds
        self.key_repeat_delay = 100  # Repeat delay in milliseconds
        self.key_timers = {"up": 0, "down": 0, "start": 0}  # Timers to track key delay
        self.key_pressed = {"up": False, "down": False, "start": False}  # Flags to track if the key is pressed
        self.GAME_W, self.GAME_H = 480, 270
        self.SCREEN_W, self.SCREEN_H = 960, 540
        self.game_canvas = pygame.Surface((self.GAME_W, self.GAME_H))
        self.screen = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.state_stack = []
        self.load_assets()
        self.load_states()
        self.MANAGER = pygame_gui.UIManager((self.SCREEN_W, self.SCREEN_H))
        pygame.display.set_caption('Arcana')


    def game_loop(self):
        while self.playing:
            self.get_events()
            self.update()
            self.render()
            pygame.time.Clock().tick(60)  # Add a frame rate limiter

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.running = False
                if event.key == pygame.K_UP:
                    self.handle_key_press('up')
                if event.key == pygame.K_DOWN:
                    self.handle_key_press('down')
                if event.key == pygame.K_BACKSPACE:
                    self.actions['back'] = True
                if event.key == pygame.K_RETURN:
                    self.handle_key_press('start')

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.handle_key_release('up')
                if event.key == pygame.K_DOWN:
                    self.handle_key_release('down')
                if event.key == pygame.K_BACKSPACE:
                    self.actions['back'] = False
                if event.key == pygame.K_RETURN:
                    self.handle_key_release('start')

    def update(self):
        self.handle_key_repeats()
        if self.state_stack:
            self.state_stack[-1].update(self.actions)
            self.reset_keys()  # Reset actions after update

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False

    def render(self):
        if self.state_stack:
            self.state_stack[-1].render(self.game_canvas)
        self.screen.blit(pygame.transform.scale(self.game_canvas, (self.SCREEN_W, self.SCREEN_H)), (0, 0))
        pygame.display.flip()

    def draw_text(self, surface, text, size, color, x, y):
        try:
            font = pygame.font.Font(self.font_path, size)
        except FileNotFoundError:
            print(f"Font file {self.font_path} not found. Using default font.")
            font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def text_input(self, x, y, sizex, sizey, color_highlighted, color_inert, actions):
        while True:
            if actions["back"]:
                print("Returning to previous menu.")
                self.exit_state()
            elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
                show_text(event.text)
        sizex = self.SCREEN_W
        sizey = self.SCREEN_H
        text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((480, 270), (460, 50)), manager=self.MANAGER, object_id="#main_text_entry")


    def load_assets(self):
        self.assets_dir = os.path.join("Assets")
        self.art_dir = os.path.join(self.assets_dir, "art")
        self.font_dir = os.path.join(self.assets_dir, "font")
        self.font_path = os.path.join(self.font_dir, "8-BIT_WONDER.TTF")
        try:
            self.font = pygame.font.Font(self.font_path, 20)
        except FileNotFoundError:
            print(f"Font file {self.font_path} not found. Using default font.")
            self.font = pygame.font.Font(None, 20)

    def load_states(self):
        self.title_screen = Title(self)
        self.title_menu = TitleMenu(self)
        self.new_game = NewGame(self)
        self.state_stack.append(self.title_screen)

    def handle_key_press(self, key):
        current_time = pygame.time.get_ticks()
        if not self.key_pressed[key]:
            # Initial press
            self.key_pressed[key] = True
            self.key_timers[key] = current_time + self.key_delay
            self.actions[key] = True
            print(f"Key {key} pressed at {current_time}")  # Debugging statement
        else:
            # Key is already pressed, update timer for repeat
            if current_time >= self.key_timers[key]:
                self.key_timers[key] = current_time + self.key_repeat_delay
                self.actions[key] = True
                print(f"Key {key} repeated at {current_time}")  # Debugging statement

    def handle_key_release(self, key):
        self.key_pressed[key] = False
        self.key_timers[key] = 0  # Reset timer on key release
        print(f"Key {key} released")  # Debugging statement

    def handle_key_repeats(self):
        current_time = pygame.time.get_ticks()
        for key in self.key_timers:
            if self.key_pressed[key] and current_time >= self.key_timers[key]:
                self.key_timers[key] = current_time + self.key_repeat_delay
                self.actions[key] = True
                print(f"Key {key} repeated at {current_time}")  # Debugging statement

if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()