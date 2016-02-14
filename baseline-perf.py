#!/usr/bin/python
import commands
import re

problemSize = 17




#Run program with different thread counts
def runSSCA(numThreads, problemSize):
    successRegex = r'Kernel 4 validation successful!'
    performanceRegex =r'TEPS score for Kernel 4 is (\d*.\d+)'
    
    cmdString = './SSCA2v2.2/SSCA2 %d %d '%(numThreads, problemSize)
    out = str(commands.getstatusoutput(cmdString))
    #print out
    
    #Check if run is sucessful
    match = re.search(successRegex, out)
    if match.group() != None:
    #Parse performance metric(TEPS)
        tepsScore = re.search(performanceRegex, out)
        return float(tepsScore.group(1))
    else:
        return None

avgScores = []
numIter = 3
threadRange = [4, 5 , 6, 7, 8]

for i in threadRange:
    totalScore = 0
    for j in range(numIter):
        results = runSSCA(i, problemSize)
        if(results != None):
            totalScore = totalScore + results
        else:
            print "Oops something went wrong"
    avg = float(totalScore) / numIter
    avgScores.append({"NumThreads": i, "avg TEPS": avg})
print avgScores


