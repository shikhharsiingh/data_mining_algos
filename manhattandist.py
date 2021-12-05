# Courtsey: sRTike
def manhattan_dist(pts):
    dims = int(len(pts) / 2)
    Sum = 0
    for i in range(dims):
        Sum += abs(pts[i] - pts[i + dims])
    return Sum