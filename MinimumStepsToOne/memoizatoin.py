# your code goes here
import time

def findMinimumStepsHelper(n,memArray):
    if(n==1):
        return memArray[1]
    else :
        if(memArray[n]==-1):
            minSteps = findMinimumStepsHelper(n-1,memArray)
            if(n%2==0):
                minSteps = min(findMinimumStepsHelper(n/2,memArray),minSteps)
            if(n%3==0):
                minSteps = min(findMinimumStepsHelper(n/3,memArray),minSteps)
            memArray[n]=1+minSteps
            return minSteps+1
        else:
            return memArray[n]

def findMinimumSteps(n):
    memArray = [-1]*(n+1)
    memArray[0],memArray[1]=0,0
    return findMinimumStepsHelper(n,memArray)

def main():
    n = int(raw_input())  # n : number for which we wish to find solution
    start = time.time()
    minSteps = findMinimumSteps(n)
    print minSteps
    print 'Execution Time:',time.time()-start,'seconds'

if __name__=='__main__':
    main()
    