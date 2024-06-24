from const import *
from GameField import QuadTree


class FieldsDotsManager:
    def __init__(self, box_manager):
        self.__method = box_manager
        self.__dots_cor = None
        self.__point = QuadTree.Point
        self.__rect = QuadTree.Rect(STANDARD_SCREEN_SIZE[0] / 2, STANDARD_SCREEN_SIZE[1] / 2,
                                    STANDARD_SCREEN_SIZE[0], STANDARD_SCREEN_SIZE[1])
        self.__qt = QuadTree.QuadTree(self.__rect)
        self.__boxes = {}
        self.__found_points = []

    def _draw(self, ax):
        self.__qt.draw(ax)

    def _get_cor_info(self):
        self.__dots_cor = self.__method.get_cor()
        if self.__dots_cor:
            return True
        return False

    def _see_region(self, cx, cy, w, h):
        return QuadTree.Rect(cx, cy, w, h)

    def _found_points(self):
        return self.__found_points

    def _chb(self):
        for dot in self.__dots_cor:
            x = dot[0]
            y = dot[1]
            point = self.__point(x, y)
            self.__boxes[(x, y)] = point
            self.__qt.insert(point)
        del point

    def _get_boxes(self):
        return self.__boxes.values()

    def _collision_dots(self, point: QuadTree.Point, radius):
        self.__qt.radius(point, radius, self.__found_points)

    def _is_collision(self, point: QuadTree.Point):
        if point in self.__found_points:
            return True
        return False

    def _in_dots(self, rect: QuadTree.Rect):
        self.__qt.neighbors(rect, self.__found_points)

    def _dhb(self):
        for dot in self.__dots_cor:
            x = dot[0]
            y = dot[1]
            self.__dots_cor = None
            self.__found_points = []
            self.__boxes[(x, y)] = 0
