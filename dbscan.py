# Courtsey: sRTike
from collections import defaultdict
import euclideandist as ed

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited, point_desc):
        visited.add(v)
        for neighbour in self.graph[v]:
            if (point_desc[v] == 'Core' or point_desc[v] == 'Boundary') and point_desc[neighbour] == "unclear":
                point_desc[neighbour] = "Boundary"
            if neighbour not in visited:
                point_desc = self.DFSUtil(neighbour, visited, point_desc)
        return point_desc

    def DFS(self, point_desc):
        visited = set()
        for vertex in self.graph:
            if vertex not in visited:
                point_desc = self.DFSUtil(vertex, visited, point_desc)
        return point_desc

def dbscan(r, n, mp, pts):
    g = Graph()
    point_desc = {}
    res = {}
    for i in range(n):
        count = 0
        desc = "Noise"
        for j in range(n):
            param = []
            for k in range(len(pts[i]) - 1):
                param.append(pts[i][k])
            for k in range(len(pts[j]) - 1):
                param.append(pts[j][k])
            dist = ed.euclidean_dist(param)
            # print(dist)
            if dist <= r:
                g.addEdge(i, j)
                if desc != "Core":    
                    desc = "unclear"
                count += 1
                if count >= mp:
                    desc = "Core"
        point_desc[pts[i][-1]] = desc
        res[pts[i][-1]] = [pts[i][k] for k in range(len(pts[i]) - 1)]
    print(res)
    point_desc = g.DFS(point_desc)
    for key in point_desc:
        if point_desc[key] == "unclear":
            res[key].append("Noise")
        else:
            res[key].append(point_desc[key])
    return res


if __name__ == "__main__":
    r = float(input("r(epsilon)= "))
    mp = int(input("Min points required= "))
    pts = []
    print("Enter the points: (in format x y z)")
    print("Enter Q after done")
    n = 0
    while True:
        row = []
        ip = input()
        row = ip.split(" ")
        if ip == "Q":
            break
        row = [float(item) for item in row]
        row.append(n)
        pts.append(row)
        n += 1
    dims = len(pts[0]) - 1
    pts_dict = dbscan(r, n, mp, pts)
    print(pts_dict)
    print("---------------------------")
    for key in pts_dict:
        for i in range(dims + 1):
            print(pts_dict[key][i], end = " ")
        print("")
