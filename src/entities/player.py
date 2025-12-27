import arcade


class Player(arcade.Sprite):
    def __init__(self, x, y, size=5):
        super().__init__()
        self.texture = arcade.make_soft_square_texture(size, arcade.color.RED, outer_alpha=255)
        self.center_x = x
        self.center_y = y
        self.speed = 5

    def update(self, delta_time: float):
        self.center_x += self.change_x
        self.center_y += self.change_y
