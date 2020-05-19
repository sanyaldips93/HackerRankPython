from itertools import product

a,b = input().split()
lista = []
listb = []

suminner = 0

for r in range(int(a)):
    lista.append(list(map(int, input().split())))

for x in product(*lista):
    for y in x:
        suminner = suminner + (y**2)
    listb.append(suminner % int(b))
    suminner = 0

print(max(listb))