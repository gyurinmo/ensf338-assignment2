import json, sys, time
import matplotlib.pyplot as plt
sys.setrecursionlimit(20000)

#improved the code by making pivot point the meddie element of the array

def func1(arr, low, high):
    if low < high:
        pivot = find_median(arr, low, high)
        pi = func2(arr, low, high, pivot)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def find_median(arr, low, high):
    mid = (high + low) // 2
    if arr[low] < arr[mid]:
        if arr[mid] < arr[high]:
            return mid
        elif arr[high] < arr[low]:
            return low
        else:
            return high
    else:
        if arr[high] < arr[mid]:
            return mid
        elif arr[low] < arr[high]:
            return low
        else:
            return high

def func2(array, start, end, pivot):
    array[start], array[pivot] = array[pivot], array[start]
    p = array[start]
    i = start + 1
    for j in range(start + 1, end + 1):
        if array[j] < p:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[start], array[i - 1] = array[i - 1], array[start]
    return i - 1


def main():
    inF = open(r'C:\Users\janem\Desktop\ensf338\assignment2\ex2.json')
    content = json.load(inF)    

    array_element = []
    for i in range(len(content)):
        array_element.append(len(content[i]))

    timelog = []

    # time log for content[0] to content[9]
    for i in range(len(content)):
        start = time.time()
        func1(content[i], 0, len(content[i])-1)
        end = time.time()
        timelog.append(end-start)


    plt.plot(array_element, timelog)
    plt.xlabel("Number of Integers")
    plt.ylabel("Execution Time")
    plt.title("Execution Time for Number of elements in an Array")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()


