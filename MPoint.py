import graphics as gr


class MPoint(gr.Point):
    def __init__(self, x, y):
        super(MPoint, self).__init__(x, y)
        self.x = x
        self.y = y

    def __eq__(self, other): return self.x == other.x and self.y == other.y

    def __ne__(self, other): return self.x != other.x or self.y != other.y