# -*- coding: utf-8 *-*
def buildGraph(myFileBuffer):
    edges = []
    for line in myFileBuffer:
        startNode = line[0:line.index(" ")]
        endNode = line[line.index(" "):]
        edges.append([startNode, endNode])
    return edges

def calculateFitness(edges, subNodes1, subNodes2, cut):
    numCuts = 0
    for edgeIter in range(len(edges)):
        tStart = int(edges[edgeIter][0])
        tEnd = int(edges[edgeIter][1])
        if tStart in subNodes1 and tEnd not in subNodes1:
            numCuts += 1
        elif tStart in subNodes2 and tEnd not in subNodes2:
            numCuts += 1
    return float(numCuts) / min(cut.count(0), cut.count(1))
