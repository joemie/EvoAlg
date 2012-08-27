import logging
import time
import sys
import random
from graph import *
from decimal import Decimal

startTime = Decimal(time.time() * 1000)
args = sys.argv[1:]

if len(args) == 0:
    print "NO CONFIG FILE SPECIFIED"
else:
    configFile = open(str(args[0]))
    configBuffer = configFile.read().splitlines()
    inFile = open(configBuffer[0])
    inFileBuffer = inFile.read().splitlines()
    if int(configBuffer[1]) == 00:
        seed = startTime
    else:
        seed = configBuffer[1]
    random.seed(seed)
    numRuns = configBuffer[2]
    logging.basicConfig(level=logging.DEBUG, filename=configBuffer[3])
    solutionFile = open(configBuffer[4], 'w')
    logging.warning("SESSION START : %s" % startTime)
    logging.warning("SESSION SEED  : %s" % seed)
    logging.warning("INPUT FILE: %s" % inFile)
    #logging.debug('in de boog')

    numNodes = inFileBuffer[0]
    numEdges = inFileBuffer[1]
    numCuts = 0
    edges = buildGraph(inFileBuffer[2:])
    bestFitness = 100
    bestCut = []
    for i in range(int(numRuns)):
        subNodes1 = []
        subNodes2 = []
        cut = []
        for j in range(int(numNodes)):
            subGroup = random.randrange(2)
            cut.append(subGroup)
            if subGroup == 0:
                subNodes1.append(j + 1)
            else:
                subNodes2.append(j + 1)
        fitness = calculateFitness(edges, subNodes1, subNodes2, cut)
        if fitness < bestFitness:
            bestFitness = fitness
            bestCut = cut
        logging.warning("RUN " + str(i) + " FITNESS: " + str(fitness))

    inFile.close
    endTime = Decimal(time.time() * 1000)
    logging.warning("SESSION END   : %s" % endTime)
    logging.warning("BEST FITNESS  : " + str(bestFitness))
    logging.warning("BEST CUT: " + str(bestCut))
    logging.warning("SESSION Length: %s" % (endTime - startTime))
    logging.warning("SESSION SEED  : %s" % seed)
    print "DONE"
