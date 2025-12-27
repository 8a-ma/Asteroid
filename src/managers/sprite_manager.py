import arcade


class SpriteManager:
    def __init__(self):
        self.player_list = arcade.SpriteList()
        self.env_list = arcade.SpriteList()

    def add_player(self, player):
        self.player_list.append(player)

    def add_environment(self, entity):
        self.env_list.append(entity)

    def update(self):
        self.player_list.update()
        self.env_list.update()

    def draw(self):
        self.env_list.draw()
        self.player_list.draw()
