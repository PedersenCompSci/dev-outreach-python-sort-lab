import os
import sys
import time
import random
from BubbleSort import bubbleSort
from InsertionSort import insertionSort
from SelectionSort import selectionSort
from QuickSort import quickSort
from MergeSort import mergeSort
from HeapSort import heapsort


def runAlgo(name, listSize):
    """
    This function will run the corresponding algorithm and record
    the running time of the algorithm.
    Argument:
        name: name of the algorithm chosen
        listSize: an integer which indicate the size of list inquired
    """
    my_randoms = list()
    for i in range (listSize):
        my_randoms.append(random.randrange(1, 101, 1))
    start = time.time()
    if name == "Bubble Sort":
        bubbleSort(my_randoms)
    elif name == "Insertion Sort":
        insertionSort(my_randoms)
    elif name == "Selection Sort":
        selectionSort(my_randoms)
    elif name == "Quick Sort":
        quickSort(my_randoms)
    elif name == "Merge Sort":
        mergeSort(my_randoms)
    elif name == "Heap Sort":
        heapsort(my_randoms)    
    end = time.time()
    timeUse = end - start
    return timeUse

def printHistogram(algoNameList, timeList):
    """
    This function will show all the actual running time of the
    corresponding algorithms in second and display a histogram by ratio
    with maximum length of 50 (can be modified) and minimum length 0.
    Argument:
        algoNameList: name of algorithm chosen
        timeList: list of running time corresponding to the algorithm
                  (with same index)
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    maxLen = 50
    maxTime = max(timeList)
    print("Running time in second:\n")
    for i in range(len(algoNameList)):
        print(algoNameList[i]+ "\t--> " + str(timeList[i]) + " s")
    
    print("\nHistogram: Time VS Algorithm\n")
    for i in range(len(algoNameList)):
        print(algoNameList[i] + "\t" + "*" * int(timeList[i] / maxTime * maxLen))


def main():
    # this list will set the name of the algorithm and it is to determine which algorithm
    algoNameList = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Quick Sort",
                "Merge Sort", "Heap Sort"]
    waitInput = True
    print("Select algorithm(s) to compare\n")
    index = 1
    for a in algoNameList:
        print(str(index) + ". " + a)
        index += 1
    print("")
    algoList = list()
    num = int(input("How many algorithm(s) do you want to compare: "))
    for i in range(num):
        choice = int(input("Algorithm's index (" + str(num - i) + " left): "))
        algoList.append(algoNameList[choice - 1])
    listSize = int(input("What size of list do you want to implement: "))
    print("Running . . .")
    timeList = list()
    for algo in algoList:
        timeList.append(runAlgo(algo, listSize))
    printHistogram(algoList, timeList)

main()
