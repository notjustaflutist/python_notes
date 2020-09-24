# September 10, 2020
# practice using turtle.Turtle() from http://greenteapress.com/thinkpython2/html/thinkpython2005.html


import turtle
import math

bob = turtle.Turtle()
alice = turtle.Turtle()
print(bob)


def square(tur, length):
    """Draw a square with a turtle object """
    for i in range(4):
        tur.fd(length)
        tur.lt(90)


def polygon(tur, n, length):
    """Draw a polygon with a turtle object """
    for i in range(n):
        tur.fd(length)
        tur.lt(360.0 / n)


def circle(tur, radius):
    """Draw an approximate circle with a turtle object """
    circumference = 2 * math.pi * radius
    n = int(circumference / 3) + 3
    '''
    Now the number of segments is an integer near circumference/3, so the length of each segment is approximately 3, 
    which is small enough that the circles look good, but big enough to be efficient, and acceptable for any size 
    circle. Adding 3 to n guarantees that the polygon has at least 3 sides. 
    '''
    length = circumference / n
    polygon(tur, n, length)


def polyline(tur, n, length, angle):
    """Draws n line segments with the given length and angle (in degrees) between them. tur is a turtle"""
    for i in range(n):
        tur.fd(length)
        tur.lt(angle)


def better_polygon(tur, n, length):
    """Draws an n sided polygon with sides of length."""
    angle = 360.0 / n
    polyline(tur, n, length, angle)


def arc(tur, radius, angle):
    """Draws an arc"""
    arc_length = 2 * math.pi * radius * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(tur, n, step_length, step_angle)


def better_circle(tur, radius):
    arc(tur, radius, 360)


'''
circle(bob, 100)
polygon(bob, n=3, length=30)  # keyword arguments make the program more readable
square(alice, 100)
better_polygon(bob, 6, 70)
better_circle(alice, 40)
arc(alice, 30, 45)
'''

turtle.mainloop()
