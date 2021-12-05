# Courtsey: sRTike
import euclideandist as eu
import numpy as np

class Point:
    def __init__(self, row) -> None:
        self._name = row[-1]
        self._coords = row[:-2]
        self._class = row[-2]

    def _print(self) -> None:
        print(self._name, ":", self._coords, "|", self._class)

def svm(dataset):
    classes = []
    for item in dataset:
        if item._class not in classes:
            classes.append(item._class)
    # print(classes)
    dists = []
    for i in range(len(dataset)):
        if dataset[i]._class == classes[0]:
            for j in range(i, len(dataset)):
                if dataset[j]._class == classes[1]:
                    dists.append([i, j, eu.euclidean_dist([dataset[i]._coords, dataset[j]._coords])])
    # print(dists)
    dists = sorted(dists, key = lambda x : x[2])
    # print(dists)
    ind = 0
    Min = dists[0][2]
    for i in range(1, len(dists)):
        if dists[i][2] > Min:
            break
        ind = i

    vecs = []
    for i in range(ind + 1):
        x = dataset[dists[i][0]]._coords.copy()
        y = dataset[dists[i][1]]._coords.copy()
        x.append(1.0)
        x.append(dataset[dists[i][0]]._class)
        y.append(1.0)
        y.append(dataset[dists[i][1]]._class)
        
        if x not in vecs:
            vecs.append(x)
        if y not in vecs:
            vecs.append(y)

    eqns = []
    deps = []
    for item in vecs:
        eqn = []
        for jtem in vecs:
            Sum = 0
            for i in range(len(item) - 1):
                Sum += (item[i] * jtem[i])
            eqn.append(Sum)
        deps.append(item[-1])
        eqns.append(eqn)
    
    ans = np.linalg.solve(eqns, deps)

    w = [0] * len(ans)
    for i in range(len(ans)):
        res = np.multiply(vecs[i][:-1], ans[i])
        w = np.add(w, res)
    w = np.round(w, 2).tolist()
    return w, ans, eqns, vecs





if __name__ == "__main__":
    dataset = []
    n = 0
    print("Enter the dataset")
    while True:
        ip = input()
        if ip == "Q":
            break
        row = ip.split(" ")
        row = [float(item) for item in row]
        row.append(n)
        dataset.append(Point(row))
        n += 1
    for item in dataset:
        item._print()
    w, ans, eqns, vecs = svm(dataset)
    print("w= ", w)
    print("Nearest Points= (last item is class)", vecs)
    print("Equations: ", eqns)
    print("Coeff.s= ", ans)