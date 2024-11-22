import pygame
from states.state import State

class Menu(State):
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.GAME_W / 2, self.game.GAME_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.game.BLACK, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.screen.blit(self.game.game_canvas, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Start'
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.get_events()
            self.check_input()
            self.game.game_canvas.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 20, self.game.WHITE, self.game.GAME_W / 2, self.game.GAME_H / 2 - 20)
            self.game.draw_text('Start Game', 20, self.game.WHITE, self.startx, self.starty)
            self.game.draw_text('Options', 20, self.game.WHITE, self.optionsx, self.optionsy)
            self.game.draw_text('Credits', 20, self.game.WHITE, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            print(f"Moved cursor to {self.state}")  # Debugging statement

        if self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            print(f"Moved cursor to {self.state}")  # Debugging statement

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False
            print(f"Selected {self.state}")  # Debugging statement

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.constrolx, self.controly = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.get_events()
            self.check_input()
            self.game.game_canvas.fill(self.game.BLACK)
            self.game.draw_text('Options', 20, self.game.GAME_W / 2, self.game.GAME_H / 2 - 30)
            self.game.draw_text('Volume', 15, self.volx, self.voly)
            self.game.draw_text('Controls', 15, self.constrolx, self.controly)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
            print("Back to Main Menu")  # Debugging statement
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.constrolx + self.offset, self.controly)
                print(f"Moved cursor to {self.state}")  # Debugging statement
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
                print(f"Moved cursor to {self.state}")  # Debugging statement
        elif self.game.START_KEY:
            # Take player to volume or controls menu.
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.get_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
                print("Back to Main Menu")  # Debugging statement
            self.game.game_canvas.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.game.GAME_W / 2, self.game.GAME_H / 2 - 20)
            self.game.draw_text('I did this', 20, self.game.GAME_W / 2, self.game.GAME_H / 2 + 10)
            self.blit_screen()