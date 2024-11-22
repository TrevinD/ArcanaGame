from states.state import State

class Options(State):
    def __init__(self, game):
        super().__init__(game)

    def enter_state(self):
        print("Entering Options State")
        pass

    def update(self, actions):
        # Handle options logic here
        pass

    def render(self, display):
        display.fill(self.game.WHITE)
        self.game.draw_text(display, "Options", 20, self.game.BLACK, self.game.GAME_W / 2, self.game.GAME_H / 2)