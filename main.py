import graphics as gr
from math import sqrt


class MPoint(gr.Point):
    def __init__(self, x, y):
        super(MPoint, self).__init__(x, y)
        self.x = x
        self.y = y

    def __eq__(self, other): return self.x == other.x and self.y == other.y

    def __ne__(self, other): return self.x != other.x or self.y != other.y


class Set:
    def __init__(self):
        self.len = 0
        self.list = []

    def insert(self, el):
        if not self.__isInside(el):
            self.list.append(el)

    def remove(self, el):
        if self.__isInside(el):
            self.list.remove(el)

    def __isInside(self, el) -> bool:
        for i in self.list:
            if i == el:
                return True
        return False

    def __iter__(self):
        self.it = iter(self.list)
        return self.it

    def __next__(self): return next(self.it)

    def __getitem__(self, item):
        return self.list[item]

    def __repr__(self):
        s = ""
        for i in self.list:
            s += str(i) + " "
        return s


def displayPoint(s, win):
    for i in s:
        i.setFill("blue")
        i.draw(win)


def displayTriangle(triangle, win):
    obj = gr.Line(triangle[0], triangle[1])
    obj.setOutline("red")
    obj.draw(win)
    obj = gr.Line(triangle[0], triangle[2])
    obj.setOutline("red")
    obj.draw(win)
    obj = gr.Line(triangle[2], triangle[1])
    obj.setOutline("red")
    obj.draw(win)


def inputPoints() -> Set:
    """s = Set()
    s.insert(MPoint(10, 10))
    s.insert(MPoint(40, 10))
    s.insert(MPoint(40, 40))
    s.insert(MPoint(30, 30))
    s.insert(MPoint(15, 20))
    s.insert(MPoint(30, 30))"""
    f = open("input.txt", "r")
    s = Set()
    n = int(f.readline())
    for i in range(n):
        x, y = f.readline().split(" ")
        s.insert(MPoint(int(x), int(y)))
    return s


def getTriangle(s) -> Set:
    triangle = Set()
    mper = 0
    mp1 = MPoint(0, 0)
    mp2 = MPoint(0, 0)
    mp3 = MPoint(0, 0)

    for first in s:
        for second in s:
            for third in s:
                ab = sqrt((second.x - first.x) ** 2 + (second.y - first.y) ** 2)
                ac = sqrt((third.x - first.x) ** 2 + (third.y - first.y) ** 2)
                bc = sqrt((third.x - second.x) ** 2 + (third.y - second.y) ** 2)
                per = ab + ac + bc
                if per > mper:
                    mper = per
                    mp1 = first
                    mp2 = second
                    mp3 = third

    triangle.insert(mp1)
    triangle.insert(mp2)
    triangle.insert(mp3)
    return triangle


if __name__ == '__main__':
    s = inputPoints()
    triangle = getTriangle(s)
    print("Треугольник максимальной площади" + str(triangle))
    win = gr.GraphWin("Окно для графики", 400, 400)
    displayPoint(s, win)
    displayTriangle(triangle, win)
    win.getMouse()  # ждём нажатия кнопки мыши
