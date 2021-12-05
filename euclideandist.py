# Courtsey: sRTike
import math
def euclidean_dist(pts):
    Sum = 0
    if len(pts) == 2:
        for i in range(len(pts[0])):
            Sum += (pts[0][i] - pts[1][i]) ** 2
    else:
        dims = int(len(pts) / 2)
        for i in range(dims):
            Sum += (pts[i] - pts[i + dims]) ** 2
    return math.sqrt(Sum)