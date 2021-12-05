# Courtsey: sRTike
import math
def information_gain(p = 0, n = 0, classes_dict = None):
    res = 0
    if classes_dict != None:
        total = 0
        for key in classes_dict:
            total += classes_dict[key]

        for key in classes_dict:
            if(classes_dict[key] == 0):
                res = 0.0
            else:
                res -= (classes_dict[key] / total) * math.log2(classes_dict[key] / total)
        return res
    res = -(p / (n + p)) * math.log2(p / (n + p)) - (n / (n + p)) * math.log2(n / (n + p))
    return res
