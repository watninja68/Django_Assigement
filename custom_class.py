class Rectance:
    def __init__(self, len: int, wid: int):
        self.len = len
        self.wid = wid

    def __iter__(self):
        yield self.len
        yield self.wid

    def print(self):
        print("Length of the rectange is :", self.len)
        print("Width of the rectange is :", self.wid)


if "__main__" == __name__:
    rectangle = Rectance(7, 3)
    rectangle.print()
    print("Iterating:")
    for dim in rectangle:
        print(dim)
