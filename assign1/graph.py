# -*- coding: utf-8 *-*
def buildGraph(myFileBuffer):
    edges = []
    for line in myFileBuffer:
        startNode = line[0:line.index(" ")]
        endNode = line[line.index(" "):]
        edges.append([startNode, endNode])
    return edges
