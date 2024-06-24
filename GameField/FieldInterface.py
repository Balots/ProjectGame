from GameField import Field


class Interface(Field.FieldsDotsManager):
    def get_cor_info(self):
        return self._get_cor_info()

    def chb(self):
        self._chb()

    def get_boxes(self):
        return self._get_boxes()

    def see_region(self, cx, cy, w, h):
        return self._see_region(cx, cy, w, h)

    def found_points(self):
        return self._found_points()

    def collision_dots(self, point, radius):
        self._collision_dots(point, radius)

    def is_collision(self, point, found_points):
        self._is_collision(point)

    def dhb(self):
        self._dhb()

    def draw(self, ax):
        self._draw(ax)

    def in_dots(self, rect):
        self._in_dots(rect)

    def get_runtime(self):
        super()._get_cor_info()
        super()._chb()
        found_points = []
        print(list(super()._get_boxes())[1])
        super()._collision_dots(list(super()._get_boxes())[1], 2)
        print(found_points)
        super()._is_collision(list(super()._get_boxes())[0])
        print(super()._get_boxes())
        super()._dhb()
