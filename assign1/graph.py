import time
import sys
import random
import os
from graph import *
from decimal import Decimal
def buildGraph(myFileBuffer):
    edges = {}
    for line in myFileBuffer:
        startNode = line[0:line.index(" ")]
        endNode = line[line.index(" ") + 1:]
        temp = []
        if edges.has_key(startNode):
            temp = list(edges.pop(startNode))
            temp.append(endNode)
            edges[startNode] = temp
        else:
            edges[startNode] = list(endNode)
        if edges.has_key(endNode):
            temp = list(edges.pop(endNode))
            temp.append(startNode)
            edges[endNode] = temp
        else:
            edges[endNode] = list(startNode)
    return edges

def calculateFitness(edges, cut):
    numCuts = 0
    for key in edges.iterkeys():
        for edgeIndex in range(len(edges[key])):
            value = edges[key][edgeIndex]
            if cut[int(key) - 1] != cut[int(value) - 1]:
                numCuts += 1
    if numCuts == 0:
        return 10000 # the graph wasn't cut so return a really large fitness
    else:
        return float(numCuts / 2) / min(cut.count('0'), cut.count('1'))

