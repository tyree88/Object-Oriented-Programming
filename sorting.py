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

#########################################################################

def printTrial(inputType, lists):
    '''
    run the trials and print the results
    '''
    
    # algorithms keys for trial
    sortType = ["bubbleSort", "insertionSort", "mergeSort", "quickSort"]
    # variables for spacing
    listsn = 3
    listLength = [10,100,1000]
    listLength.sort()

    print()
    #HEADER#
    print("Input type =",inputType)
    print()
    print("                   avg time      avg time     avg time")
    print("Sort Function      (n = 10)      (n = 100)   (n = 1000)")
    print("-----------------------------------------------------------")
    for sort in sortType:
        print(" " + sort.ljust(14), end = "")
        for n in listLength:
            myList = []
            myList.append(n)
            print("    ", "%.6f" % runTrial(sort, myList), end = "")          
        print()

    print()

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



def almostSorted(lst):
    #Create the sorted list then use n = 10% of the length of the list
    # so for list length 100, this should make 10 random swaps
    [lst[i].sort() for i in range(3)]
    index = [[random.randint(0, 9) for x in range(2)]]
    index.append([random.randint(0, 99) for x in range(11)])
    index.append([random.randint(0, 999) for x in range(101)])
    #enumerate through the list
    #holds the numbers and element in the index
    for l, indexList in enumerate(index):
         for x in range(len(indexList)//2-1):
                i = indexList[x*2]
                j = indexList[x*2+1]
                # x != j 
                while i == j:
                     i = random.randint(0,len(lst[l])-1)
                #swap
                lst[l][i], lst[l][j] = lst[l][j], lst[l][i]
    return lst
    
    newlst = []
    while len(newlst)//2 < elements:
        int1 = random.randint(0,len(lst)-1)
        int2 = random.randint(0,len(lst)-1)
        #cant have the same numbers 
        if int1 == int2:
            continue
        if (int2 in newlst) and not (int1 in newlst):
            newlst.append(int1)
            newlst.append(int2)
            temp = lst[int1]
            lst[int1] = lst[int2]
            lst[int2] = temp
    return lst

def main():
    # tests
    tests = ["Random", "Sorted", "Reverse", "Almost sorted"]
    
    allLists = [
    [i for i in range(10)],
    [i for i in range(100)],
    [i for i in range(1000)]]

    for inputType in tests:
        if inputType =="Random":
                for i in range(3):
                    
                    newlist = [random.shuffle(allLists[i])]
                    

        if inputType =="Sorted":
                for i in range(3):
                    newlist = [allLists[i].sort()]

        if inputType =="Reverse":
                for i in range(3):
                    newlist = list(reversed(allLists[i]))

        if inputType =="Almost sorted":
                for i in range(3):
                    newlist = [almostSorted(allLists)]
            
        printTrial(inputType, newlist )


main()

    
