def group(aList):
    intList = [aList[0]]
    lenList = []
    k = 1
    for i in range(1,len(aList)):
        if aList[i] != aList[i-1]:
            lenList.append(k)
            intList.append(aList[i])
            k = 1
        else:
            k = k+1
    lenList.append(k)
    return intList, lenList

listA, listB = group(list(map(int, input().split())))
print(listA, '\n', listB)
