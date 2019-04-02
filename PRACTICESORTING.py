#  File: sorting.py
#  Description: Compares different sorting algorithms
#  Student's Name: Charles Lybrand
#  Student's UT EID: cbl652
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: 04/07/2017
#  Date Last Modified: 04/08/2017


################### GIVE CODE ###################
    
import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

################### END GIVE CODE ###################

class RandomList:
    '''
    Create an n-length list of sorted numbers
    Several methods create certain "shuffled" versions of the list
    '''
    
    # init a sorted list
    def __init__(self, n):
        self.length = n
        self.list = list(range(1, n+1))
        
    # randomize the list
    def random(self):
        random.shuffle(self.list)
        
    # recreate the list in sorted order
    def sort(self):
        self.list = list(range(1, self.length+1))
        
    # reverse the list
    def reverse(self):
        self.list = list(reversed(self.list))
        
    # shuffle 10% of the list
    def almostSorted(self):
        elements = self.length//10
        indices = []
        while len(indices)//2 < elements:
            rand1 = random.randint(0,self.length-1)
            rand2 = random.randint(0,self.length-1)
            # if the numbers are the same, restart process
            if rand1 == rand2:
                continue
            # proceed if the new random numbers are unique from previous numbers
            if not ( (rand1 in indices) and (rand2 in indices) ):
                # swap list[rand1] with list[rand2]
                indices.append(rand1); indices.append(rand2)
                temp = self.list[rand1]
                self.list[rand1] = self.list[rand2]
                self.list[rand2] = temp
                
    def __str__(self):
        return str(self.list)

def runTrial(alg, myList):
    '''
    Run and time a given sorting algorithm on a specified list
    5 times and return the average 
    '''
    
    trials = 5
    elapsedTime = 0.0
    
    # time Bubble Sort
    if(alg == "bubbleSort"):
        for i in range(trials):
            startTime = time.time()
            bubbleSort(myList)
            endTime = time.time()
            elapsedTime += endTime - startTime
    # time Selection Sort
    elif(alg == "selectionSort"):
        for i in range(trials):
            startTime = time.time()
            selectionSort(myList)
            endTime = time.time()
            elapsedTime += endTime - startTime
    # time Insert Sort
    elif(alg == "insertionSort"):
        for i in range(trials):
            startTime = time.time()
            insertionSort(myList)
            endTime = time.time()
            elapsedTime += endTime - startTime
    # time Merge Sort
    elif(alg == "mergeSort"):
        for i in range(trials):
            startTime = time.time()
            mergeSort(myList)
            endTime = time.time()
            elapsedTime += endTime - startTime
    # time Quick Sort
    elif(alg == "quickSort"):
        for i in range(trials):
            startTime = time.time()
            quickSort(myList)
            endTime = time.time()
            elapsedTime += endTime - startTime 
    
    # return the average
    return elapsedTime/trials
        
    
def printTrial(inputType, lists):
    '''
    run the trials and print the results
    '''
    
    # algorithms keys for trial
    algs = ["bubbleSort", "selectionSort", "insertionSort", "mergeSort", "quickSort"]
    
    # variables for spacing
    space = " "*3
    col1 = 14
    col2 = 8
    listsn = len(lists)
    lengths = list(lists.keys())
    lengths.sort()
    
    print()
    
    # create and print the header
    print("Input type = %s" % (inputType))
    header = space + ' '*col1
    for i in range(listsn):
        header += space + "avg time".center(col2)
    header += "\n"
    header += space + "Sort function".ljust(col1)
    for i in range(listsn):
        header += space + ("(n=%d)" % lengths[i]).center(col2)
    header += "\n"
    header += "-"*53
    
    print(header)
    
    print()
    
    for alg in algs:
        print(space + alg.ljust(col1), end="")
        
        for n in lengths:
            # make a copy of the list
            myList = lists[n].list[:]
            print(space + "%.6f" % runTrial(alg, myList), end="")
            
        print()

    print()
    
def main():
    
    # tests
    tests = ["Random", "Sorted", "Reverse", "Almost sorted"]
    
    lists = {}
    for i in range(1, 4):
        n = 10**i
        l = RandomList(n)
        lists[n] = l
    print(lists)
    
        
    for inputType in tests:
        # adjust list for each sorting algorithm
        if(inputType == "Random"):
            for l in lists:
                lists[l].random()

        elif(inputType == "Sorted"):
            for l in lists:
                lists[l].sort()
        elif(inputType == "Reverse"):
            for l in lists:
                lists[l].reverse()
        elif(inputType == "Almost sorted"):
            for l in lists:
                # make sure list is sorted first
                lists[l].sort()
                lists[l].almostSorted()
                
        # print the results for specific inputType
        printTrial(inputType, lists)
    
    
if __name__ == "__main__":
    main()
