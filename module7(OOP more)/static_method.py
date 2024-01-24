from math import *
class Pizza:
    @staticmethod
    def Area(radius):
        area = pi * (radius ** 2)
        print('Area of Pizza is:', round(area, 4))

Pizza.Area(5)

