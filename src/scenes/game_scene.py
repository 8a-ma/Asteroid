import arcade
import math
from entities.star import Star
from entities.player import Player
from managers.sprite_manager import SpriteManager


class GameScene:
    def __init__(self, window, manager):
        self.window = window
        self.manager = manager
        self.screen_center_x = self.window.width // 2
        self.screen_center_y = self.window.height // 2

        self.sprite_manager = SpriteManager()

        self.player = None
        self.start = None

    def setup(self):
        self.player = Player(self.screen_center_x // 2, self.screen_center_y)
        self.star = Star(self.screen_center_x, self.screen_center_y, mass=10, size=10)

        self.sprite_manager.add_player(self.player)
        self.sprite_manager.add_environment(self.star)

    def _apply_gravity(self):
        """Calcula la atracción entre la estrella y el jugador."""
        diff_x = self.star.center_x - self.player.center_x
        diff_y = self.star.center_y - self.player.center_y
        distance = math.sqrt(diff_x**2 + diff_y**2)
        k = 10

        pull = k * (self.star.mass * self.player.mass) / (distance ** 2) if distance != 0 else 0
        # Normalizar y aplicar
        self.player.change_x += (diff_x / distance) * pull
        self.player.change_y += (diff_y / distance) * pull

    def on_draw(self):
        self.sprite_manager.draw()

    def on_update(self, delta_time: float):
        self._apply_gravity()
        self.sprite_manager.update()

    def on_key_press(self, key: int, modifiers: int):
        self.update_player_input(key, True)

    def on_key_release(self, key: int, modifiers: int):
        self.update_player_input(key, False)

    def update_player_input(self, key, state):
        if key == arcade.key.W: self.player.move = self.player.move._replace(up=state)
        elif key == arcade.key.S: self.player.move = self.player.move._replace(down=state)
        elif key == arcade.key.A: self.player.move = self.player.move._replace(left=state)
        elif key == arcade.key.D: self.player.move = self.player.move._replace(right=state)
