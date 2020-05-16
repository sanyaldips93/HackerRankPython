import sys
a = list(map(int, input().split()))


cyclev = a[0]//2
cycleh = a[1]

for i in range(cyclev):
    print((('.|.')*((2*i)+1)).center(cycleh, '-'))
print('WELCOME'.center(cycleh, '-'))
for i in range(cyclev):
    print((('.|.')*((2*(cyclev-i-1))+1)).center(cycleh, '-'))