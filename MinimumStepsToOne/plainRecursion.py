# your code goes here
import time
start = 0

def findMinimumStepsHelper(n):
    if(n==1):
        return 0
    else :
        minSteps = findMinimumStepsHelper(n-1)
        if(n%2==0):
            minSteps = min(findMinimumStepsHelper(n/2),minSteps)
        if(n%3==0):
            minSteps = min(findMinimumStepsHelper(n/3),minSteps)
        return minSteps+1


def findMinimumSteps(n):
    return findMinimumStepsHelper(n)

def main():
    n = int(raw_input())  # n : number for which we wish to find solution
    start = time.time()
    minSteps = findMinimumSteps(n)
    print minSteps
    print 'Execution Time:',time.time()-start,'seconds'

if __name__=='__main__':
    main()
    