import pygame

from player_character import CharacterCreation
from states.state import State
from menu import Menu



class NewGame(State):
    def __init__(self, game):
        super().__init__(game)
        self.title = "Character Creation"
        self.menu_options = ["Create a Character", "Back", "Quit"]
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
        if selected_option == "Create a Character":
            new_state = CharacterCreation(self.game)
            new_state.enter_state()
            print("Create a character")
        elif selected_option == "Back":
            self.exit_state()
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