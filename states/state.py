# states/state.py

class State:
    def __init__(self, game):
        self.game = game
        self.prev_state = None

    def update(self, actions):
        pass

    def render(self, surface):
        pass

    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)

    def exit_state(self):
        if self.game.state_stack:
            self.game.state_stack.pop()
            if self.game.state_stack and hasattr(self.game.state_stack[-1], 'text_input_active'):
                self.game.state_stack[-1].text_input_active = False
                self.game.state_stack[-1].exit_text_input()