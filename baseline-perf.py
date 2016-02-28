#!/usr/bin/python
import commands
import re
import sys

problemSize = 17
MIN_THREAD = 1
MAX_THREAD = 20

#Run program with different thread counts
def runSSCA(executableName, numThreads, problemSize):
    successRegex = r'Kernel 4 validation successful!'
    performanceRegex =r'TEPS score for Kernel 4 is (\d*.\d+)'
    
    cmdString = '%s %d %d '%(executableName, numThreads, problemSize)
    out = str(commands.getstatusoutput(cmdString))
    print out 
    #Check if run is sucessful
    match = re.search(successRegex, out)
    if match.group() != None:
    #Parse performance metric(TEPS)
        tepsScore = re.search(performanceRegex, out)
        return float(tepsScore.group(1))
    else:
        return None
def computeAvg(executableName):
    avgScores = []
    numIter = 3
    threadRange = [x for x in range(MIN_THREAD, MAX_THREAD+1)]

    for i in threadRange:
        totalScore = 0
        #print "Running iteration %d"%(i)
        for j in range(numIter):
            results = runSSCA(executableName, i, problemSize)
            if(results != None):
                totalScore = totalScore + results
            else:
                print "Oops something went wrong"
        avg = float(totalScore) / numIter
        #avgScores.append({"NumThreads": i, "avg TEPS": avg})
        avgScores.append(avg)
    print avgScores

if __name__ == "__main__":
    executable = sys.argv[1] #i.e ./SSCA2
    computeAvg(executable)
