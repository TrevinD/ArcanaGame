import pygame

from states.state import State
#from player_character import CharacterCreation
from menu import Menu


class NewGame(State, Menu):
    def __init__(self, game):
        State.__init__(self, game)
        Menu.__init__(self, game)
        self.menu_options = ["Create a New Character", "Back"]
        self.selected_index = 0
        self.vertical_offset = 60  # Vertical offset for the entire menu
        self.white_space = 25
        self.offset = -20  # Offset for the cursor
        self.option_positions = self.calculate_option_positions()

    def calculate_option_positions(self):
        # Calculate the positions of each menu option
        positions = []
        num_options = len(self.menu_options)
        start_y = (self.game.GAME_H // 2 - (
                    num_options * self.white_space) // 2) + self.vertical_offset  # Center the menu vertically with offset
        for i, option in enumerate(self.menu_options):
            text = self.game.font.render(option, True, self.game.BLACK)
            text_rect = text.get_rect(center=(self.game.GAME_W // 2, start_y + i * self.white_space))  # Space options 25 pixels apart
            positions.append(text_rect)
        return positions

    def move_cursor(self, actions):
        if actions['down']:
            self.selected_index = (self.selected_index + 1) % len(self.menu_options)
            print(f"Moved cursor to {self.menu_options[self.selected_index]} at {pygame.time.get_ticks()}")  # Debugging statement

        if actions['up']:
            self.selected_index = (self.selected_index - 1) % len(self.menu_options)
            print(f"Moved cursor to {self.menu_options[self.selected_index]} at {pygame.time.get_ticks()}")  # Debugging statement

    def update(self, actions,):
        self.move_cursor(actions)
        if actions["start"]:
            selected_option = self.menu_options[self.selected_index]
            if selected_option == "Create a New Character":
                new_state = CharacterCreation(self.game)
                new_state.enter_state()
            elif selected_option == "Back":
                print("Returning to previous menu.")
                self.exit_state()

            print(f"Selected {selected_option}")  # Debugging statement

    def render(self, display):
        display.fill(self.game.WHITE)
        self.game.draw_text(display, "Character Creation", 20, self.game.BLACK, self.game.GAME_W / 2, self.game.GAME_H / 2 - 60)

        # Draw each menu option
        for i, option in enumerate(self.menu_options):
            self.game.draw_text(display, option, 15, self.game.BLACK, self.option_positions[i].centerx,
                                self.option_positions[i].centery)

        # Draw the cursor next to the selected option
        self.draw_cursor(display)

    def draw_cursor(self, display):
        cursor_x = self.option_positions[self.selected_index].left + self.offset
        cursor_y = self.option_positions[self.selected_index].centery - 5
        pygame.draw.line(display, self.game.BLACK, (cursor_x, cursor_y), (cursor_x, cursor_y + 10), 2)