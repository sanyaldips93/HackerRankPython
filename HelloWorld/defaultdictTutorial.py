from collections import defaultdict
a,b = map(int, input().split())
d = defaultdict(list)

for i in range(a):
    d['aList'].append(input())

for j in range(b):
    d['bList'].append(input())
    for ij in range(a):
        if d['aList'][ij] == d['bList'][j]:
            d[str(j+1)+'Index'].append(ij+1)

for j in range(b):
    if(len(d[str(j+1)+'Index'])) == 0:
        print(-1)
    else:
        print(*d[str(j+1)+'Index'], sep=' ')
