from states.state import State

class Credits(State):
    def __init__(self, game):
        super().__init__(game)

    def enter_state(self):
        print("Entering Credits State")
        self.game.push_state(self)

    def update(self, actions):
        # Handle credits logic here
        pass

    def render(self, display):
        display.fill(self.game.WHITE)
        self.game.draw_text(display, "Credits", 20, self.game.BLACK, self.game.GAME_W / 2, self.game.GAME_H / 2)