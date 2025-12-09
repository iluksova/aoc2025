import pathlib
from collections import deque
from dataclasses import dataclass
from functools import cached_property


@dataclass
class Point:
    x: int
    y: int

    def __repr__(self):
        return f'({self.x}, {self.y})'

class Line:
    def __init__(self, start: Point, end: Point):
        swap=False
        if start.x > end.x:
            swap=True
        elif start.x == end.x and start.y >= end.y:
            swap=True
        if swap:
            self.start = end
            self.end = start
        else:
            self.start = start
            self.end = end

    @cached_property
    def is_vertical(self) -> bool:
        return self.start.x == self.end.x

    def __repr__(self):
        return f'Line({self.start} -> {self.end})'


class Rectangle:
    def __init__(self, a: Point, b: Point):
        self.a_1 = a
        self.b_1 = b
    def __repr__(self):
        return f'Rec({self.a_1}, {Point(self.b_1.x, self.a_1.y)}, {self.b_1}, {Point(self.a_1.x, self.b_1.y)})'

    def size(self) -> int:
        x_l = self.xs[1] - self.xs[0] + 1
        y_l = self.ys[1] - self.ys[0] + 1
        return x_l * y_l

    @cached_property
    def xs(self) -> tuple[int, int]:
        if self.a_1.x <= self.b_1.x:
            return self.a_1.x, self.b_1.x
        else:
            return self.b_1.x, self.a_1.x

    @cached_property
    def ys(self) -> tuple[int, int]:
        if self.a_1.y <= self.b_1.y:
            return self.a_1.y, self.b_1.y
        else:
            return self.b_1.y, self.a_1.y

    def intersects(self, line: Line):
        if line.is_vertical:
            if line.start.y >= self.ys[1] or line.end.y <= self.ys[0]:
                return False

            if self.xs[1] <= line.start.x or line.end.x <= self.xs[0]:
                return False
            return True
        else:
            if line.start.x >= self.xs[1] or line.end.x <= self.xs[0]:
                return False

            if self.ys[1] <= line.start.y or line.end.y <= self.ys[0]:
                return False
            return True


rec = Rectangle(Point(2, 2), Point(5, 5))
assert rec.intersects(Line(Point(3, 3), Point(3, 5))) == True
assert rec.intersects(Line(Point(3, 5), Point(3, 8))) == False
assert rec.intersects(Line(Point(2, 0), Point(2, 3))) == False
assert rec.intersects(Line(Point(3, 0), Point(3, 3))) == True
assert rec.size() == 16

rec2 = Rectangle(Point(2, 5), Point(11, 1))
assert rec2.intersects(Line(Point(7, 3), Point(7, 1))) == True

lines = pathlib.Path('_input/9/input.txt').open('r').readlines()
lines = [line.strip() for line in lines]

coords = [line.split(',') for line in lines]
points = [Point(int(x), int(y)) for x, y in coords]

rectangles =[]
max = 1
for i, a in enumerate(points):
    for j, b in enumerate(points):
        if i < j:
            rec = Rectangle(a, b)
            rectangles.append(rec)
            size = rec.size()
            if size > max:
                max = size

print(f'Part1: {max}')

shifted = deque(points)
shifted.rotate(-1)
lines = [Line(start, end) for start, end in zip(points, list(shifted))]

max = 1
for rec in rectangles:
    intersects = False
    for l in lines:
        if rec.intersects(l):
            intersects = True
            break

    if not intersects:
        size = rec.size()
        if size > max:
            max = size

print(f'Part2: {max}')



