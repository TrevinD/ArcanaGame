from states.state import State
from ui.ui_elements import TextInputBox
# character_creation.py (updated)

class CharacterCreation(State):
    def __init__(self, game):
        super().__init__(game)
        self.character_name = ""
        self.name_confirmed = False
        self.text_input_box = TextInputBox(40, 135, 400, 30,
                                            on_confirm_callback=self.on_name_confirmed)

    def handle_events(self, events):
        for event in events:
            self.text_input_box.handle_event(event, self.game)

    def render(self, surface):
        surface.fill(self.game.BLACK)
        self.game.draw_text(surface, "Enter Character Name", 20, self.game.WHITE, self.game.GAME_W // 2, 100)
        self.text_input_box.draw(surface)

    def on_name_confirmed(self, name):
        self.character_name = name
        self.name_confirmed = True
        print(f"Character name confirmed: {self.character_name}")
        # You can add additional logic here to proceed to the next state
        self.exit_state()