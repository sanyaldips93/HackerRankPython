N = int(input())
A = []
for _ in range(N):
    command, *line = input().split()
    inputs = list(map(int, line))
    if command == 'insert':
        A.insert(inputs[0], inputs[1])
    elif command == 'print':
        print(A)
    elif command == 'remove':
        A.remove(inputs[0])
    elif command == 'append':
        A.append(inputs[0])
    elif command == 'sort':
        A.sort()
    elif command == 'reverse':
        A.reverse()
    elif command == 'pop':
        A.pop()

