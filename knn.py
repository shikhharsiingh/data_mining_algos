# Courtsey: sRTike
import euclideandist as ed

class point:
    def __init__(self, coords, _class, name) -> None:
        self.coords = []
        for item in coords:
            self.coords.append(item)
        self._class = _class
        self.name = name
    
    def _print(self):
        print(self.name, ":", self.coords, "|", self._class)

def knn(pts, query, k):
    if len(query) != len(pts[0]) - 2:
        print("Dimensions mismatch.")
        return {}
    Points = []
    for row in pts:
        Points.append(point(row[:-2], row[-2], row[-1]))
    for item in Points:
        item.Print()
    dists = []
    for i in range(len(Points)):
        dists.append([i,ed.euclidean_dist([Points[i].coords, query])])
    dists = sorted(dists, key = lambda x :  x[1])
    #Uncomment the following to print the respective distances of the query point with all the points
    # print(dists) 
    classes = {}
    Max = 0
    classification = None
    for i in range(k):
        if Points[dists[i][0]]._class not in classes.keys():
            classes[Points[dists[i][0]]._class] = 1
        else:
            classes[Points[dists[i][0]]._class] += 1
            if classes[Points[dists[i][0]]._class] >= Max:
                Max = classes[Points[dists[i][0]]._class]
                classification = Points[dists[i][0]]._class
    return classification, Max

if __name__ == "__main__":
    pts = []
    print("Enter the points: (in format, x y z class)")
    print("Enter Q after done")
    n = 0
    while True:
        row = []
        ip = input()
        values = ip.split(" ")
        if ip == "Q":
            break
        for item in values[:-1]:
            row.append(float(item))
        row.append(values[-1])
        row.append(n)
        pts.append(row)
        n += 1
    print("Enter query point: ")
    query = []
    ip = input()
    query = ip.split(" ")
    query = [float(item) for item in query]
    while len(query) != (len(pts[0]) - 2):
        print("Dimensions mismatch.")
        query = []
        ip = input()
        query = ip.split(" ")
        query = [float(item) for item in query]
    k = int(input("k= "))
    classification, vote = knn(pts, query, k)
    print("Class :", classification, "Votes:", vote)