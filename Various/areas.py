
# Dimentions of triangle

import math
from math import pi

lenght = int(input('Triangle lenght? '))
height = int(input('Triangle height? '))
areaTriangle = (lenght*height)*(0.5)
print("Area Triangle =", areaTriangle)

radius = int(input('Circle radius? '))
areaCircle = pi*(radius**2)
print("Area Triangle =", areaCircle)

lenght = int(input('Rectangle lenght? '))
height = int(input('Rectangle height? '))
perimeterRectangle = (lenght+height)*2
print("Perimeter Rectangle =", perimeterRectangle)

side = int(input('Square side? '))
if side < 0:
    print('Error! The value cannot be negative')
else:
    areaSquare = side**2
    print('Area square =', areaSquare)


