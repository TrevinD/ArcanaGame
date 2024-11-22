from states.state import State

class LoadGame(State):
    def __init__(self, game):
        super().__init__(game)

    def enter_state(self):
        print("Entering Load Game State")
        self.game.push_state(self)

    def update(self, actions):
        # Handle load game logic here
        pass

    def render(self, display):
        display.fill(self.game.WHITE)
        self.game.draw_text(display, "Load Game", 20, self.game.BLACK, self.game.GAME_W / 2, self.game.GAME_H / 2)