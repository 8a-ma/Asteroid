import arcade
from config.config import Config
from core.game import GameWindow


if __name__ == '__main__':
    config = Config()
    window = GameWindow(config.width, config.height, config.title)

    arcade.run()
