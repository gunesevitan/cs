# Chapter Fifteen Exercises



# Exercise 15.1
# Write a function called distance_between_points that takes two Points as arguments
# and returns the distance between them.



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point_a = Point(10, 20)
point_b = Point(2, 5)


def distance_between_points(point1, point2):
    return ((point1.x - point2.x),(point1.y - point2.y))

print(distance_between_points(point_a, point_b))



# Exercise 15.2
# Write a function named move_rectangle that takes a Rectangle and two numbers
# named dx and dy. It should change the location of the rectangle by adding dx to the x
# coordinate of corner and adding dy to the y coordinate of corner.


class Rectangle:
    def __init__(self, width, height, point):
        self.width = width
        self.height = height
        self.corner = point


point_c = Point(50, 150)
rectangle_a = Rectangle(100, 200, point_c)


def move_rectangle(rectangle, x, y):
    rectangle.point.x += x
    rectangle.point.y += y



# Exercise 15.3
# Write a version of move_rectangle that creates and returns a new Rectangle instead of
# modifying the old one.



from copy import deepcopy


def move_rectangle_new(rectangle, x, y):
    copied_rectangle = deepcopy(rectangle)
    copied_rectangle.corner.x += x
    copied_rectangle.corner.y += y
    return copied_rectangle