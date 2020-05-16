neslist = []
count = int(input())
for _ in range(count):
        name = input()
        score = float(input())
        neslist.append([name, score])

# print(neslist)
values = [k[1] for k in neslist]
i = 0
maxival = max(values)

while i<count:
    if values[i] == maxival:
        values.remove(values[i])
        i = -1
        count = count - 1
    i=i+1;

maxival = max(values)
length = len(values)
j = 0

while j<length:
    if values[j] == maxival:
        values.remove(values[j])
        j = -1
        length = length - 1
    j=j+1;

maxival = max(values)
length = len(values)
j = 0
print(values)
while j<length:
    if values[j] == maxival:
        name = [k[0] for k in neslist if k[1] == values[j]]
    j = j+1

for k in name:
    print(k)