class StateManager:
    def __init__(self, window):
        self.window = window
        self.current_scene = None

    def setup(self):
        pass

    def draw(self):
        if self.current_scene:
            self.current_scene.on_draw()

    def update(self, delta_time: float):
        if self.current_scene:
            self.current_scene.on_updated(delta_time)

    def on_key_press(self, key: int, modifiers: int):
        pass

    def on_key_release(self, key: int, modifiers: int):
        pass
