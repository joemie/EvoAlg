#import logging
#logging.basicConfig(level=logging.DEBUG, filename=configBuffer[3])
#logging.debug('in de boog')
import time
import sys
import random
import os
from graph import *
from arena import *
from decimal import Decimal


startTime = Decimal(time.time() * 1000)
args = sys.argv[1:]
configFile = None
if len(args) == 0:
    configFile = open("default.cfg")
elif os.path.isfile(str(args[0])):
    configFile = open(str(args[0]))
else:
    print "INVALID CONFIG FILE"
    sys.exit()
configBuffer = configFile.read().splitlines()
inFile = open(configBuffer[0])
inFileBuffer = inFile.read().splitlines()
logFile = open(str(configBuffer[4]), 'a+')
if int(configBuffer[1]) == 00:
    seed = startTime
else:
    seed = configBuffer[1]
random.seed(seed)
numRuns = configBuffer[2]
numEvals = configBuffer[3]
logFile = open(str(configBuffer[4]), 'a+')
solutionFile = open(str(configBuffer[5]), 'a+')
pSelType = str(configBuffer[6]).partition("|")[0].strip()
if(pSelType == "tournament"):
    pTournSize = str(configBuffer[6].partition("|")[2])
else:
    pTournSize = None
recombType = str(configBuffer[7]).partition("|")[0].strip()
if(recombType == "npoint"):
    numSplits = str(configBuffer[7].partition("|")[2])
else:
    numSplits = None
survivalType = str(configBuffer[8]).partition("|")[0].strip()
if(survivalType == "tournament"):
    survivalTournSize = str(configBuffer[8].partition("|")[2])
else:
    survivalTournSize = None
parentSize = int(configBuffer[9])
childrenSize = int(configBuffer[10])

print configFile
print logFile
logFile.write("SESSION START : %s" % startTime + "\n")
logFile.write("SESSION SEED  : %s" % seed + "\n")
logFile.write("CONFIG FILE : %s" % inFile + "\n")
logFile.write("SURVIVAL SELECTION: %s" % survivalType + "\n")
logFile.write("PARENT SELECTION : %s" % pSelType + "\n")
logFile.write("RECOMBINATION: %s" % recombType + "\n")
logFile.write("MUTATION: BIT FLIP")
logFile.write("POPULATION SIZE: " + str(parentSize) + "\n")
logFile.write("OFFSPRING SIZE: " + str(childrenSize) + "\n")
numNodes = inFileBuffer[0]
numEdges = inFileBuffer[1]
numCuts = 0
edges = buildGraph(inFileBuffer[2:])
bestCut = []
population = initPopulation(500, 8)
selectParents(edges, population, childrenSize, pSelType, survivalTournSize)
for i in range(int(numRuns)):
    bestFitness = float("-inf")
    logFile.write("RUN: " + str(i + 1) + "\n")
    print("RUN: " + str(i + 1))
    for j in range(int(numEvals) + 1):
        subNodes1 = []
        subNodes2 = []
        cut = list(bin(random.randrange(2 ** (int(numNodes) - 1), 2 ** int(numNodes)))[2:])
        #tTime = Decimal(time.time() * 1000)
        fitness = calculateFitness(edges, cut)
        #print "CALC FIT: " + str(Decimal(time.time() * 1000) - tTime)
        if fitness > bestFitness:
            bestFitness = fitness
            bestCut = cut
            logFile.write('\t' + str(j + 1) + '\t' + str(fitness) + '\n')
solutionFile.write(str(bestFitness * -1) + "\n")
solutionFile.write(str(bestCut) + "\n")
solutionFile.close()
inFile.close
endTime = Decimal(time.time() * 1000)
logFile.write("SESSION END   : %s" % endTime + "\n")
logFile.write("SESSION Length: %s" % (endTime - startTime) + "\n")

logFile.close()
print "DONE"
