# Courtsey: sRTike
import manhattandist as md

def cdist(pts, i):
    ans = []
    for j in range(len(pts)):
        param = []
        for k in range(len(pts[i]) - 1):
            param.append(pts[i][k])
        for k in range(len(pts[j]) - 1):
            param.append(pts[j][k])
        ans.append(md.manhattan_dist(param))
    return ans

def kmedoid(k, pts):
    l = len(pts)
    c_dists = {}

    # We, first take out the cost of every point from every other point
    for i in range(l):
        c_dists[pts[i][-1]] = cdist(pts, i)
    # print(c_dists) #To view the different distance of each point from every other point, uncomment

    #Next, we take add the minimum respective costs between every point pair as if they were the assumed medoids
    res = []
    for i in range(l):
        for j in range(i + 1, l):
            temp = []
            temp.append(i)
            temp.append(j)
            ans = 0
            for t in range(l):
                ans += min(c_dists[i][t], c_dists[j][t])
            temp.append(ans)
            res.append(temp)
    res = sorted(res, key = lambda x: x[2])
    # print(res)  #To see the different medoid pair costs, uncomment

    # We find the lowest cost medoid pair
    least = res[0]
    medoids = {}
    medoids[least[0]] = []
    medoids[least[1]] = []
    medoids["sum"] = least[2]

    # We make points cluster based on these medoids
    for i in range(l):
        if c_dists[least[0]][i] < c_dists[least[1]][i]:
            medoids[least[0]].append(i)
        else:
            medoids[least[1]].append(i)
    return medoids

if __name__ == "__main__":
    k = int(input("k= "))
    pts = []
    print("Enter the points: (in x y z format)")
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
    medoids = kmedoid(k, pts)
    print("---------------------------")
    print("Medoids and Clusters")
    for key in medoids:
        print(key, medoids[key])