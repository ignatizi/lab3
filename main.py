from math import pi
class Sphere:
    def __init__(self, *arg):
        if len(arg) == 0:
            arg = (1, 0, 0, 0)
        self.r = arg[0]
        self.x = arg[1]
        self.y = arg[2]
        self.z = arg[3]
    def get_volume(self):
        return (self.r ** 3) * pi * 4 / 3
    def get_square(self):
        return (self.r ** 2) * pi * 4
    def get_radius(self):
        return self.r
    def get_center(self):
        return (self.x, self.y, self.z)
    def set_radius(self, r):
        self.r = r
    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def is_point_inside(self, x, y, z):
        mf = (self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2
        rad = self.r ** 2
        if mf < rad:
            return True
        else:
            return False