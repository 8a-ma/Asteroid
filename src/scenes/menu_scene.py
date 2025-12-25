import arcade
from scenes.game_scene import GameScene


class MenuScene:
    def __init__(self, window, manager):
        self.window = window
        self.manager = manager

        self.screen_center_x = self.window.width // 2
        self.screen_center_y = self.window.height // 2

    def setup(self):
        pass

    def on_draw(self):
        arcade.draw_text(
            "PRESIONA ENTER PARA JUGAR",
            self.screen_center_x,
            self.screen_center_y,
            arcade.color.WHITE, 20, anchor_x="center"
        )

    def on_update(self, delta_time: float):
        pass

    def on_key_press(self, key: int, modifiers: int):

        if key == arcade.key.ENTER:
            self.manager.change_scene(GameScene)

    def on_key_release(self, key: int, modifiers: int):
        pass
