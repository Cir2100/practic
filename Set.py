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