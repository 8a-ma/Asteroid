import arcade
from entities.player import Player


class GameScene:
    def __init__(self, window, manager):
        self.window = window
        self.manager = manager
        self.player = None
        self.player_list = arcade.SpriteList()

        self.screen_center_x = self.window.width // 2
        self.screen_center_y = self.window.height // 2

    def setup(self):
        self.player = Player(self.screen_center_x, self.screen_center_y)

        self.player_list.append(self.player)

    def on_draw(self):
        self.player_list.draw()

    def on_update(self, delta_time: float):
        self.player_list.update()

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.W:
            self.player.move = self.player.move._replace(up=True)
        elif key == arcade.key.S:
            self.player.move = self.player.move._replace(down=True)
        elif key == arcade.key.A:
            self.player.move = self.player.move._replace(left=True)
        elif key == arcade.key.D:
            self.player.move = self.player.move._replace(right=True)

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.W:
            self.player.move = self.player.move._replace(up=False)
        elif key == arcade.key.S:
            self.player.move = self.player.move._replace(down=False)
        elif key == arcade.key.A:
            self.player.move = self.player.move._replace(left=False)
        elif key == arcade.key.D:
            self.player.move = self.player.move._replace(right=False)
