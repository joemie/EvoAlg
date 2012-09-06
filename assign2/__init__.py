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
solutionFile = open(str(configBuffer[5]), 'a+')
parentSelType = str(configBuffer[6])
recombType = str(configBuffer[7])
survivalType = str(configBuffer[8])

print configFile
print logFile
logFile.write("SESSION START : %s" % startTime + "\n")
logFile.write("SESSION SEED  : %s" % seed + "\n")
logFile.write("CONFIG FILE : %s" % inFile + "\n")
logFile.write("PARENT SELECTION : %s" % parentSelType + "\n")
logFile.write("RECOMBINATION: %s" % recombType + "\n")
logFile.write("MUTATION: BIT FLIP")
logFile.write("SURVIVAL SELECTION: %s" % survivalType + "\n")
numNodes = inFileBuffer[0]
numEdges = inFileBuffer[1]
numCuts = 0
edges = buildGraph(inFileBuffer[2:])
bestCut = []
population = initPopulation(5, 8)

for i in range(int(numRuns)):
    bestFitness = 100
    logFile.write("RUN: " + str(i + 1) + "\n")
    print("RUN: " + str(i + 1))
    for j in range(int(numEvals) + 1):
        subNodes1 = []
        subNodes2 = []
        cut = list(bin(random.randrange(2 ** (int(numNodes) - 1), 2 ** int(numNodes)))[2:])
        #tTime = Decimal(time.time() * 1000)
        fitness = calculateFitness(edges, cut)
        #print "CALC FIT: " + str(Decimal(time.time() * 1000) - tTime)
        if fitness < bestFitness:
            bestFitness = fitness
            bestCut = cut
            logFile.write('\t' + str(j + 1) + '\t' + str(fitness) + '\n')
solutionFile.write(str(bestFitness) + "\n")
solutionFile.write(str(bestCut) + "\n")

solutionFile.close()
inFile.close
endTime = Decimal(time.time() * 1000)
logFile.write("SESSION END   : %s" % endTime + "\n")
logFile.write("SESSION Length: %s" % (endTime - startTime) + "\n")

logFile.close()
print "DONE"
