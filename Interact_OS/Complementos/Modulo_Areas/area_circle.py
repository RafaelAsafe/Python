import math

def circle(radius):
    return math.pi*(radius**2)

def donuts(outside_radius, inside_radius):
    return circle(outside_radius) - circle(inside_radius)

