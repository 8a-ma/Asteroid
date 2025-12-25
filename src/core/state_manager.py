from scenes.menu_scene import MenuScene
from scenes.game_scene import GameScene


class StateManager:
    def __init__(self, window):
        self.window = window
        self.current_scene = MenuScene(self.window, self)

    def setup(self):
        if self.current_scene:
            self.current_scene.setup()

    def draw(self):
        self.current_scene.on_draw()

    def update(self, delta_time: float):
        self.current_scene.on_updated(delta_time)

    def on_key_press(self, key: int, modifiers: int):
        self.current_scene.on_key_press(key, modifiers)

    def on_key_release(self, key: int, modifiers: int):
        self.current_scene.on_key_release(key, modifiers)

    def change_scene(self, new_scene_class):
        self.current_scene = new_scene_class(self.window, self)
        self.current_scene.setup()
