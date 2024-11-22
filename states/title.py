from states.state import State

class Title(State):
    def __init__(self, game):
        super().__init__(game)
        from states.titlemenu import TitleMenu
        self.title_menu = TitleMenu(game)

    def update(self, actions):
        if actions["start"]:
            from states.titlemenu import TitleMenu
            new_state = TitleMenu(self.game)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((255,255,255))
        self.game.draw_text(display,"Arcana", 20, (0,0,0), self.game.GAME_W/2, self.game.GAME_H/2)
