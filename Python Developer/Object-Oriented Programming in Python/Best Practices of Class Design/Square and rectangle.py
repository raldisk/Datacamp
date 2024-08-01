# 1/4
class Rectangle:
    def __init__(self, h, w):
        self.h = h
        self.w = w


# Define a Square class
class Square(Rectangle):
    def __init__(self, w):
        Rectangle.__init__(self, w, w)


# 2/4
# The 4x4 Square object would no longer be a square if we assign 7 to h.


# 3/4
class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h

    # Define set_h to set h
    def set_h(self, h):
        self.h = h

    # Define set_w to set w
    def set_w(self, w):
        self.w = w


class Square(Rectangle):
    def __init__(self, w):
        self.w, self.h = w, w

    # Define set_h to set w and h
    def set_h(self, h):
        self.h = h
        self.w = h

    # Define set_w to set w and h
    def set_w(self, w):
        self.w = w
        self.h = w


# 4/4
# Each of the setter methods of Square change both h and w attributes, while setter methods of Rectangle change only one attribute at a time, so the Square objects cannot be substituted for Rectangle into programs that rely on one attribute staying constant.
