def insertionSort(aList):
    temp = 0
    for i in range(1, len(aList)):
        key = aList[i]
        j = i - 1
        while j>=0 and aList[j]>key:
            aList[j+1] = aList[j]
            j = j -1
        aList[j+1] = key
    return aList


a = list(map(int, input().split()))
print(insertionSort(a))
