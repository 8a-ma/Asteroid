import arcade



class Quadtree:
    def __init__(self, boundary: arcade.Rect, capacity: int):
        self.boundary = boundary
        self.capacity = capacity
        self.entities = []
        self.divided = False

        self.northwest = None
        self.northeast = None
        self.southwest = None
        self.southeast = None

    def subdivide(self):
        x, y, w, h = self.boundary.left, self.boundary.bottom, self.boundary.width, self.boundary.height
        hw, hh = w / 2, h / 2

        self.northeast = Quadtree(arcade.rect.XYWH(x + w * 1.5, y + h * 1.5, w, h), self.capacity)
        self.northwest = Quadtree(arcade.rect.XYWH(x + w * 0.5, y + h * 1.5, w, h), self.capacity)
        self.southeast = Quadtree(arcade.rect.XYWH(x + w * 1.5, y + h * 0.5, w, h), self.capacity)
        self.southwest = Quadtree(arcade.rect.XYWH(x + w * 0.5, y + h * 0.5, w, h), self.capacity)

        self.divided = True

    def _contains(self, entity):
        """Comprueba si un punto está dentro de los límites del cuadrante."""
        return (self.boundary.left <= entity.center_x < self.boundary.right and self.boundary.bottom <= entity.center_y < self.boundary.top)

    def _intersects(self, range_rect):
        """Comprueba si un rectángulo de búsqueda se solapa con este cuadrante."""
        return not (range_rect.left > self.boundary.right or range_rect.right < self.boundary.left or range_rect.top < self.boundary.bottom or range_rect.bottom > self.boundary.top)

    def insert(self, entity):
        if not self._contains(entity):
            return False

        if len(self.entities) < self.capacity:
            self.entities.append(entity)
            return True

        if not self.divided:
            self.subdivide()

        return (self.northeast.insert(entity) or
                self.northwest.insert(entity) or
                self.southeast.insert(entity) or
                self.southwest.insert(entity))

    def query(self, range_rect, found):
        if not self._intersects(range_rect):
            return found

        for entity in self.entities:
            if (range_rect.left <= entity.center_x <= range_rect.right and
                range_rect.bottom <= entity.center_y <= range_rect.top):
                found.append(entity)

        if self.divided:
            self.northwest.query(range_rect, found)
            self.northeast.query(range_rect, found)
            self.southwest.query(range_rect, found)
            self.southeast.query(range_rect, found)
        return found
