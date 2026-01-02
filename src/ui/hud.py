import arcade


class HUD:
    def __init__(self, window, player):
        self.window = window
        self.player = player

        self.label = arcade.Text(
            "",
            x=20,
            y=15,
            color=arcade.color.WHITE,
            font_size=12,
            font_name="Kenney Future"
        )

    def update(self):
        pass

    def draw(self):
        dashboard_color = (0, 0, 0, 160)

        arcade.draw_lrbt_rectangle_filled(
            left=0,
            right=self.window.width,
            top=40,
            bottom=0,
            color=dashboard_color
        )

        velocity = (self.player.change_x**2 + self.player.change_y**2)**0.5
        self.label.text = f"Velocidad: {velocity:.2f} | Pos: {int(self.player.center_x)}, {int(self.player.center_y)}"
        self.label.draw()

        arcade.draw_line(0, 40, self.window.width, 40, arcade.color.GOLD, 2)
