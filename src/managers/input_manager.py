import arcade


class InputManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InputManager, cls).__new__(cls)
            cls._instance.keys = set()

        return cls._instance

    def key_press(self, key):
        self.keys.add(key)

    def key_release(self, key):
        if key in self.keys:
            self.keys.remove(key)

    def is_pressed(self, key):
        return key in self.keys
