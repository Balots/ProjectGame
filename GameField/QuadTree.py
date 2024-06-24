import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def collision(self, other):
        try:
            other_x, other_y = other.x, other.y
        except AttributeError:
            other_x, other_y = other
        return np.hypot(self.x - other_x, self.y - other_y)


class Rect:
    def __init__(self, cx, cy, w, h):
        self.cx = cx
        self.cy = cy
        self.w = w
        self.h = h
        self.west_edge, self.east_edge = cx - w / 2, cx + w / 2
        self.north_edge, self.south_edge = cy - h / 2, cy + h / 2

    def dot_contains(self, point: Point):
        try:
            point_x, point_y = point.x, point.y
        except AttributeError:
            point_x, point_y = point

        return (self.west_edge <= point_x < self.east_edge and
                self.north_edge <= point_y < self.south_edge)

    def intersect(self, other):
        return not (other.west_edge > self.east_edge or
                    other.east_edge < self.west_edge or
                    other.north_edge > self.south_edge or
                    other.south_edge < self.north_edge)

    def draw(self, ax, c='k', lw=1, **kwargs):
        x1, y1 = self.west_edge, self.north_edge
        x2, y2 = self.east_edge, self.south_edge
        print(x1, x2, y1, y2)
        ax.plot([x1,x2,x2,x1,x1],[y1,y1,y2,y2,y1], c=c, lw=lw, **kwargs)


class QuadTree:
    def __init__(self, rect: Rect, max_points=4, depth=0):
        self.rect = rect
        self.max_points = max_points
        self.depth = depth
        self.points = []
        self.divided = False

    def divide(self):
        cx, cy = self.rect.cx, self.rect.cy
        w, h = self.rect.w / 2, self.rect.h / 2
        self.nw = QuadTree(Rect(cx - w / 2, cy - h / 2, w, h), self.max_points, self.depth + 1)
        self.ne = QuadTree(Rect(cx + w / 2, cy - h / 2, w, h), self.max_points, self.depth + 1)
        self.se = QuadTree(Rect(cx + w / 2, cy + h / 2, w, h), self.max_points, self.depth + 1)
        self.sw = QuadTree(Rect(cx - w / 2, cy + h / 2, w, h), self.max_points, self.depth + 1)
        self.divided = True

    def insert(self, point):
        if not self.rect.dot_contains(point):
            return False
        if len(self.points) < self.max_points:
            self.points.append(point)
            return True
        if not self.divided:
            self.divide()

        return (self.nw.insert(point) or
                self.ne.insert(point) or
                self.sw.insert(point) or
                self.se.insert(point))

    def neighbors(self, rect: Rect, found_points: list):
        if not self.rect.intersect(rect):
            return False
        for point in self.points:
            if rect.dot_contains(point):
                found_points.append(point)
        if self.divided:
            self.nw.neighbors(rect, found_points)
            self.ne.neighbors(rect, found_points)
            self.se.neighbors(rect, found_points)
            self.sw.neighbors(rect, found_points)
        return found_points

    def circle(self, rect: Rect, point: Point, radius, found_points: list):
        centre = (point.x, point.y)
        if not self.rect.intersect(rect):
            return False
        for p in self.points:
            if p is point:
                continue
            if rect.dot_contains(p) and 0 < p.collision(centre) <= radius:
                found_points.append(p)

        if self.divided:
            self.nw.circle(rect, point, radius, found_points)
            self.ne.circle(rect, point, radius, found_points)
            self.sw.circle(rect, point, radius, found_points)
            self.se.circle(rect, point, radius, found_points)
        return found_points

    def radius(self, point: Point, radius, found_points):
        centre = (point.x, point.y)
        rect = Rect(*centre, 2 * radius, 2 * radius)
        return self.circle(rect, point, radius, found_points)

    def __len__(self):
        npoints = len(self.points)
        if self.divided:
            npoints += len(self.nw) + len(self.ne) + len(self.se) + len(self.sw)
        return npoints

    def draw(self, ax):
        self.rect.draw(ax)
        if self.divided:
            self.nw.draw(ax)
            self.ne.draw(ax)
            self.se.draw(ax)
            self.sw.draw(ax)
