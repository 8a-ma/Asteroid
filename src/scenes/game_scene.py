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
            self.player.change_y = self.player.speed
        elif key == arcade.key.S:
            self.player.change_y = -self.player.speed
        elif key == arcade.key.A:
            self.player.change_x = -self.player.speed
        elif key == arcade.key.D:
            self.player.change_x = self.player.speed

    def on_key_release(self, key: int, modifiers: int):
        if key in (arcade.key.W, arcade.key.S):
            self.player.change_y = 0
        if key in (arcade.key.A, arcade.key.D):
            self.player.change_x = 0
        pass
