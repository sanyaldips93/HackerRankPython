
x = int(input())
y = int(input())
z = int(input())
n = int(input())


list_cord = [];
cord = [];
for i in range(x):
    for j in range(y):
        for k in range(z):
                cord = [i,j,k];
                list_cord.append(cord);

print(list_cord);
