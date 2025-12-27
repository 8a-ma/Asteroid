import arcade
from core.state_manager import StateManager


class GameWindow(arcade.Window):
    def __init__(self, width: int = 200, heigth: int = 200, title: str = "Windows"):
        super().__init__(width, heigth, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.state_manager = StateManager(self)

    def setup(self):
        self.state_manager.setup()

    def on_draw(self):
        self.clear()
        self.state_manager.draw()

    def on_update(self, delta_time: float):
        self.state_manager.update(delta_time)

    def on_key_press(self, key: int, modifiers: int):
        self.state_manager.on_key_press(key, modifiers)

    def on_key_release(self, key: int, modifiers: int):
        self.state_manager.on_key_release(key, modifiers)
