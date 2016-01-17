# your code goes here
import time

def findMinimumSteps(n):
    memArray = [-1]*(n+1)
    memArray[0],memArray[1]=0,0
    for i in range(2,n+1):
        minSteps = memArray[i-1]+1
        if(i%2==0):
            minSteps = min(memArray[i/2]+1,minSteps)
        if(i%3==0):
            minSteps = min(memArray[i/3]+1,minSteps)
        memArray[i]=minSteps
    return memArray[n]

def main():
    n = int(raw_input())  # n : number for which we wish to find solution
    start = time.time()
    print findMinimumSteps(n)
    print 'Execution time:',time.time()-start,'seconds'

if __name__=='__main__':
    main()