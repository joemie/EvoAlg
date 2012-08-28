#import logging
#logging.basicConfig(level=logging.DEBUG, filename=configBuffer[3])
#logging.debug('in de boog')
import time
import sys
import random
import os
from graph import *
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
print configFile
configBuffer = configFile.read().splitlines()
inFile = open(configBuffer[0])
inFileBuffer = inFile.read().splitlines()
logFile = open(str(configBuffer[3]), 'a+')
if int(configBuffer[1]) == 00:
    seed = startTime
else:
    seed = configBuffer[1]
random.seed(seed)
numRuns = configBuffer[2]
solutionFile = open(str(configBuffer[4]), 'a+')
print configFile
print logFile
logFile.write("SESSION START : %s" % startTime + "\n")
logFile.write("SESSION SEED  : %s" % seed + "\n")
logFile.write("INPUT FILE: %s" % inFile + "\n")

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
    tTime = Decimal(time.time() * 1000)
    for j in range(int(numNodes)):
        subGroup = random.randrange(2)
        cut.append(subGroup)
        if subGroup == 0:
            subNodes1.append(j + 1)
        else:
            subNodes2.append(j + 1)
    print "LOAD CUT: " + str(Decimal(time.time() * 1000) - tTime)
    tTime = Decimal(time.time() * 1000)
    fitness = calculateFitness(edges, subNodes1, subNodes2, cut)
    print "CALC FIT: " + str(Decimal(time.time() * 1000) - tTime)
    if fitness < bestFitness:
        bestFitness = fitness
        bestCut = cut
        print bestFitness
        logFile.write("RUN " + str(i) + "\nFITNESS: " + str(fitness) + "\n")

inFile.close
endTime = Decimal(time.time() * 1000)
logFile.write("SESSION END   : %s" % endTime + "\n")
logFile.write("BEST FITNESS  : " + str(bestFitness) + "\n")
logFile.write("BEST CUT: " + str(bestCut) + "\n")
logFile.write("SESSION Length: %s" % (endTime - startTime) + "\n")
logFile.write("SESSION SEED  : %s" % seed + "\n")
solutionFile.write(str(bestFitness) + "\n")
solutionFile.write(str(bestCut) + "\n")
solutionFile.close()
print "DONE"
