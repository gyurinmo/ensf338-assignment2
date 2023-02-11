import json, sys, time
import matplotlib.pyplot as plt
sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:                                                  
        pi = func2(arr, low, high)                                   
        func1(arr, low, pi-1)                                       
        func1(arr, pi + 1, high)                                     

def func2(array, start, end):
    p = array[start]                                                 
    low = start + 1                                                  
    high = end                                                       
    while True:
        while low <= high and array[high] >= p:                     
            high = high - 1                                          
        while low <= high and array[low] <= p:                       
            low = low + 1                                            
        if low <= high:                                             
            array[low], array[high] = array[high], array[low]        
        else:
            break
        
    array[start], array[high] = array[high], array[start]            
    return high                                                      


def main():
    inF = open(r'C:\Users\janem\Desktop\ensf338\assignment2\ex2.json')
    content = json.load(inF)    

    array_element = []
    for i in range(3):
        array_element.append(len(content[i]))

    timelog = []

    # time log for content[0] to content[9]
    for i in range(3):
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


