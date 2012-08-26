import logging
import time
import sys
import random
from graph import *
from decimal import Decimal

startTime = Decimal(time.time() * 1000)
cut = []
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
    logging.warning("---RUN START : %s" % startTime)
    logging.warning("---RUN SEED  : %s" % seed)
    logging.warning("---INPUT FILE: %s" % inFile)
    #logging.debug('in de boog')

    numNodes = inFileBuffer[0]
    numEdges = inFileBuffer[1]
    numCuts = 0
    edges = buildGraph(inFileBuffer[2:])
    subNodes1 = []
    subNodes2 = []

    for i in range(int(numNodes)):
        subGroup = random.randrange(2)
        cut.append(subGroup)
        if subGroup == 0:
            subNodes1.append(i + 1)
        else:
            subNodes2.append(i + 1)

    print edges
    print cut
    print subNodes1
    print subNodes2

    fitness = calculateFitness(edges, subNodes1, subNodes2, cut)
    print fitness
    inFile.close

    endTime = Decimal(time.time() * 1000)
    logging.warning("---RUN END   : %s" % endTime)
    logging.warning("---RUN Length: %s" % (endTime - startTime))
    logging.warning("---RUN SEED  : %s" % seed)
    print "DONE"
