#Greg Brewer
# 5/28/2023
# Problem 1 area of circle function

import math

def areaOfCircle(r):
    area = math.pi * math.pow(r, 2)
    return area

radius = 5
circle_area = areaOfCircle(radius)
print(f"The area of a circle with radius {radius} is {circle_area}.")

