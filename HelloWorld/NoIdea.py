# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = list(map(int, input().split()))

lista = list(map(int, input().split()))
seta = set(map(int, input().split()))
setb = set(map(int, input().split()))



count = 0

print(sum((a in seta) - (a in setb) for a in lista))