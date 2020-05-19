n = int(input())
s = set(map(int, input().split()))

opnum = int(input())

for i in range(opnum):
    command, *operand = input().split()
    ops = list(map(int, operand))

    if command == 'pop' and len(s) != 0:
        s.pop()
    elif command == 'remove':
        if ops[0] in s:
            s.remove(ops[0])
    elif command == 'discard':
        s.discard(ops[0])
print(sum(s))
