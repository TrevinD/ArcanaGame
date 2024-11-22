import pygame

class Menu:
    def __init__(self, game):
        self.game = game
        self.menu_options = []
        self.selected_index = 0
        self.vertical_offset = 60  # Vertical offset for the entire menu
        self.white_space = 25
        self.offset = -20  # Offset for the cursor
        self.option_positions = self.calculate_option_positions()

    def calculate_option_positions(self):
        positions = []
        num_options = len(self.menu_options)
        start_y = (self.game.GAME_H // 2 - (num_options * self.white_space) // 2) + self.vertical_offset
        for i, option in enumerate(self.menu_options):
            text = self.game.font.render(option, True, self.game.BLACK)
            text_rect = text.get_rect(center=(self.game.GAME_W // 2, start_y + i * self.white_space))
            positions.append(text_rect)
        return positions

    def move_cursor(self, actions):
        if actions['down']:
            self.selected_index = (self.selected_index + 1) % len(self.menu_options)
            print(f"Moved cursor to {self.menu_options[self.selected_index]} at {pygame.time.get_ticks()}")

        if actions['up']:
            self.selected_index = (self.selected_index - 1) % len(self.menu_options)
            print(f"Moved cursor to {self.menu_options[self.selected_index]} at {pygame.time.get_ticks()}")

    def handle_selection(self):
        selected_option = self.menu_options[self.selected_index]
        print(f"Selected {selected_option}")  # Debugging statement
        # Implement logic for handling each menu option

    def render(self, display):
        display.fill(self.game.WHITE)
        self.game.draw_text(display, self.title, 20, self.game.BLACK, self.game.GAME_W / 2, self.game.GAME_H / 2 - 60)

        for i, option in enumerate(self.menu_options):
            self.game.draw_text(display, option, 15, self.game.BLACK, self.option_positions[i].centerx,
                                self.option_positions[i].centery)

        self.draw_cursor(display)

    def draw_cursor(self, display):
        cursor_x = self.option_positions[self.selected_index].left + self.offset
        cursor_y = self.option_positions[self.selected_index].centery - 5
        pygame.draw.line(display, self.game.BLACK, (cursor_x, cursor_y), (cursor_x, cursor_y + 10), 2)