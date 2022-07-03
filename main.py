import graphics as gr
from math import sqrt
from Set import Set
from MPoint import MPoint


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
    print("Треугольник максимальной площади: " + str(triangle))
    win = gr.GraphWin("Точечки", 600, 600)
    displayPoint(s, win)
    displayTriangle(triangle, win)
    win.getMouse()  # ждём нажатия кнопки мыши
