import arcade
import math
from random import randint, uniform
from entities.player import Player
from entities.entities import Star
from entities.entities import Asteroid
from managers.sprite_manager import SpriteManager


class GameScene:
    def __init__(self, window, manager):
        self.window = window
        self.manager = manager
        self.screen_center_x = self.window.width // 2
        self.screen_center_y = self.window.height // 2

        self.sprite_manager = SpriteManager(self.window)

        self.player = None
        self.start = None
        self.num_asteroid = 10

    def setup(self):
        self.player = Player(self.screen_center_x // 2, self.screen_center_y)
        self.sprite_manager.add_player(self.player)

        self.star = Star(self.screen_center_x, self.screen_center_y, mass=10, size=10)
        self.sprite_manager.add_environment(self.star)

        for _ in range(self.num_asteroid):
            x, y = randint(0, self.window.width), randint(0, self.window.height)
            asteroid = Asteroid(x, y, mass=uniform(0, 10), size=randint(3, 10))
            asteroid.init_velocity_towards(self.screen_center_x * 1.1, self.screen_center_y * 1.1)
            self.sprite_manager.add_astroid(asteroid)

    def apply_mutual_gravity(self, actor, target):
        """Calcula la atracción entre la estrella y el jugador."""
        diff_x = target.center_x - actor.center_x
        diff_y = target.center_y - actor.center_y
        distance_sq = diff_x**2 + diff_y**2
        distance = math.sqrt(distance_sq)

        if distance < 30:
            return

        force_magnitude = (actor.mass * target.mass) / distance_sq
        # Normalizar y aplicar
        k = 10
        actor.change_x += (diff_x / distance) * force_magnitude * k
        actor.change_y += (diff_y / distance) * force_magnitude * k

    def on_draw(self):
        self.sprite_manager.draw()

    def on_update(self, delta_time: float):
        entities = []
        entities.extend(self.sprite_manager.player_list)
        entities.extend(self.sprite_manager.asteroid_list)
        entities.extend(self.sprite_manager.env_list)

        for idx_i, entitie_i in enumerate(entities):
            if getattr(entitie_i, 'static', False): continue

            for idx_j, entitie_j in enumerate(entities):
                if idx_i == idx_j: continue

                self.apply_mutual_gravity(entitie_i, entitie_j)

        self.sprite_manager.update()

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.ESCAPE:
            from scenes.menu_scene import MenuScene

            self.manager.change_scene(MenuScene)

    def on_key_release(self, key: int, modifiers: int):
        pass
