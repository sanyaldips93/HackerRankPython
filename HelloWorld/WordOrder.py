# ---------imports--------
from collections import OrderedDict, defaultdict
# ---------imports--------


aList = []
aDict = {}

for k in range(int(input())):
    aList.append(input())

for i in range(len(aList)):
    count = 1
    for j in range(i+1, len(aList)):
        if aList[j] == aList[i]:
            count = count + 1
            aList[j] = None

    aDict[aList[i]] = count

aDict.pop(None)
print(*aDict.values(), sep=' ')


# Using OrderedDict

# words = OrderedDict()
#
# for i in range(int(input())):
#     word = input()
#     if word not in words:
#         words[word] = 1
#     else:
#         words[word] = words[word] + 1
#
# print(len(words.keys()))
# print(*words.values(), end='')

# Using defaultdict

# words = defaultdict(int)
#
# for i in range(int(input())):
#     word = input()
#     words[word] = words[word] + 1
#
# print(len(words.keys()))
# print(*words.values(), end='')
