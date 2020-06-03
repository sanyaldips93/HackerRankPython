int(input())
b = list(map(int, input().split()))
print(len(list(filter(lambda x: x > 0, b))) == len(b) and len(list(filter(lambda x: str(x) == str(x)[::-1], b))) > 0)


# Alternative
# print all([int(i)>0 for i in b]) and any([j == j[::-1] for j in b])
