from itertools import groupby

sequence = list(map(int, input().split()))

lenList = []
intList = []

for a,b in groupby(sequence):
    intList.append(a)
    lenList.append(len([*b]))

if len(intList) > len(set(intList)) or len(lenList) > len(set(lenList)):
    print(False)
else:
    print(True)


