import random
from operator import itemgetter
import sys

def initPopulation(popSize, strSize):
    pop = []
    for i in range(popSize):
        pop.append(list(bin(random.randrange(2 ** (int(strSize) - 1), 2 ** int(strSize)))[2:]))
    return pop

def selectParents(edges, population, childrenSize, selType, tournSize = None):
    selected = []  #list of indexes in the popualtion
    if selType == "tournament" and tournSize != None:
        for i in range(int(childrenSize)):
            tournSelect = []
            for j in range(int(tournSize)):
                popIndex = random.randint(0, len(population) - 1)
                appendMe = {"index" : popIndex , "fitness": calculateFitness(edges, population[popIndex]) * -1}
                tournSelect.append(appendMe)
            tournSelect = sorted(tournSelect, key=itemgetter('fitness'))
            print tournSelect
    elif selType == "tournament" and tournSize == None:
        print "INVALID TOURNAMENT SIZE - EXITING"
        sys.exit()
    return selected

def calculateFitness(edges, cut):
    numCuts = 0
    for key in edges.iterkeys():
        for edgeIndex in range(len(edges[key])):
            value = edges[key][edgeIndex]
            if cut[int(key) - 1] != cut[int(value) - 1]:
                numCuts += 1
    if numCuts == 0:
        return float("-inf")  # the graph wasn't cut so return infinity
    else:
        return float(numCuts / 2) / min(cut.count('0'), cut.count('1')) * -1
