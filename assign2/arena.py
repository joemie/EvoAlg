import random


def initPopulation(popSize, strSize):
    pop = []
    for i in range(popSize):
        pop.append(list(bin(random.randrange(2 ** (int(strSize) - 1), 2 ** int(strSize)))[2:]))
    return pop

def calculateFitness(edges, cut):
    numCuts = 0
    for key in edges.iterkeys():
        for edgeIndex in range(len(edges[key])):
            value = edges[key][edgeIndex]
            if cut[int(key) - 1] != cut[int(value) - 1]:
                numCuts += 1
    if numCuts == 0:
        return float("inf")  # the graph wasn't cut so return infinity
    else:
        return float(numCuts / 2) / min(cut.count('0'), cut.count('1'))

