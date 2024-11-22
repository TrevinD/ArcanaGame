import pygame
from states.state import State
from menu import Menu
from states.new_game import NewGame
from states.load_game import LoadGame  # Ensure you have this module
from states.options import Options  # Ensure you have this module
from states.credits import Credits  # Ensure you have this module

class TitleMenu(State):
    def __init__(self, game):
        super().__init__(game)
        self.title = "Title Menu"
        self.menu_options = ["New Game", "Continue Game", "Options", "Credits", "Quit"]
        self.selected_index = 0
        self.vertical_offset = 60  # Vertical offset for the entire menu
        self.white_space = 25
        self.offset = -20  # Offset for the cursor
        self.menu = Menu(game)
        self.menu.title = self.title
        self.menu.menu_options = self.menu_options
        self.menu.selected_index = self.selected_index
        self.menu.vertical_offset = self.vertical_offset
        self.menu.white_space = self.white_space
        self.menu.offset = self.offset
        self.menu.option_positions = self.menu.calculate_option_positions()

    def move_cursor(self, actions):
        self.menu.move_cursor(actions)
        self.selected_index = self.menu.selected_index

    def handle_selection(self):
        selected_option = self.menu_options[self.selected_index]
        if selected_option == "New Game":
            new_state = NewGame(self.game)
            new_state.enter_state()
        elif selected_option == "Continue Game":
            new_state = LoadGame(self.game)
            new_state.enter_state()
        elif selected_option == "Options":
            new_state = Options(self.game)
            new_state.enter_state()
        elif selected_option == "Credits":
            new_state = Credits(self.game)
            new_state.enter_state()
        elif selected_option == "Quit":
            print("Exiting Game")
            self.game.playing = False
            self.game.running = False
        print(f"Selected {selected_option}")  # Debugging statement

    def update(self, actions):
        self.move_cursor(actions)
        if actions["start"]:
            self.handle_selection()

    def render(self, display):
        self.menu.render(display)