import math as m
import sys


def commonPointsOfTwoCircles(x1, y1, x2, y2, r1, r2):
    if (r1 + r2 > m.sqrt(m.pow(x2 - x1, 2) + m.pow(y2 - y1, 2))):
        return True
    else:
        return False


def commonPointsOfTwoSpheres(x1, y1, z1, x2, y2, z2, r1, r2):
    if (r1 + r2 > m.sqrt(m.pow(x2 - x1, 2) + m.pow(y2 - y1, 2) + m.pow(z2 - z1, 2))):
        return True
    else:
        return False


def smallerCircleArea(r1, r2):
    rSmaller = min(r1, r2)
    return m.pi * rSmaller * rSmaller


def calcAreaIntersectingCircles(d, r1, r2):
    r1sqr = r1 * r1
    r2sqr = r2 * r2

    # if the circle centers are the same
    if d == 0:
        print('\nCircles have the same center. Intersecting area will be area of smaller circle')
        return smallerCircleArea(r1, r2)

    angle1 = (r1sqr + (d * d) - r2sqr) / (2 * r1 * d)
    angle2 = (r2sqr + (d * d) - r1sqr) / (2 * r2 * d)

    # Check to see if the circles are overlapping
    if ((angle1 < 1 and angle1 >= -1) or (angle2 < 1 and angle2 >= -1)):
        theta1 = (m.acos(angle1) * 2)
        theta2 = (m.acos(angle2) * 2)

        area1 = (0.5 * theta2 * r2sqr) - (0.5 * r2sqr * m.sin(theta2))
        area2 = (0.5 * theta1 * r1sqr) - (0.5 * r1sqr * m.sin(theta1))

        return area1 + area2
    elif angle1 == 1 and angle2 == 1:
        print('\nCircles touch at a single point and do not intersect\n')
        return 0
    elif angle1 < -1 or angle2 < -1:
        print(
            '\nSmaller circle is completely inside the larger circle. Intersecting area will be area of smaller circle')
        return smallerCircleArea(r1, r2)
    else:
        print('\nImaginary touch points\n')
        return -1


x1 = 0
y1 = 0
x2 = 2
y2 = 0
radiusCircle1 = 2
radiusCircle2 = 2

distance = m.sqrt(m.pow(x2 - x1, 2) + m.pow(y2 - y1, 2))
if distance < 0 or radiusCircle1 < 0 or radiusCircle2 < 0:
    print('Values cannot be negative')

print(calcAreaIntersectingCircles(distance, radiusCircle1, radiusCircle2))
