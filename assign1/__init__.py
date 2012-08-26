import logging
import time
import random
from graph import *
from decimal import Decimal

logging.basicConfig(level = logging.DEBUG, filename= 'log.txt')

startTime = Decimal(time.time() * 1000)
mySeed = 1
myCut = []
random.seed(mySeed)

myFile = open(r'C:\Users\joseph\MiscDev\Python\EvoAlg\assign1\dataFiles\example.dat')
myFileBuffer = myFile.read().splitlines()
logging.warning("---RUN START : %s" % startTime)
logging.warning("---RUN SEED  : %s" % mySeed)
logging.warning("---INPUT FILE: %s" % myFile)
#logging.debug('in de boog')

numNodes = myFileBuffer[0]
numEdges = myFileBuffer[1]
numCuts = 0
myEdges = buildGraph(myFileBuffer[2:])
subNodes1 = []
subNodes2 = []
for i in range(int(numNodes)):
    subGroup = random.randrange(2)
    myCut.append(subGroup)
    if subGroup == 0:
        subNodes1.append(i + 1)
    else:
        subNodes2.append(i + 1)
print myEdges
print myCut
print subNodes1
print subNodes2

for edgeIter in range(len(myEdges)):
    tStart = int(myEdges[edgeIter][0])
    tEnd = int(myEdges[edgeIter][1])
    if tStart in subNodes1 and tEnd not in subNodes1:
        numCuts += 1
    elif tStart in subNodes2 and tEnd not in subNodes2:
        numCuts += 1
print float(numCuts) / min(myCut.count(0), myCut.count(1))
myFile.close

endTime = Decimal(time.time() * 1000)
logging.warning("---RUN END   : %s" % endTime)
logging.warning("---RUN Length: %s" % (endTime - startTime))
logging.warning("---RUN SEED  : %s" % mySeed)
print "DONE"
