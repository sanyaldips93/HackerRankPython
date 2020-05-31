from collections import OrderedDict

dicta = OrderedDict()
for i in range(int(input())):
    string = list(input().split())
    num = string.pop()
    string = ' '.join(string)
    if string in dicta.keys():
        dicta[string] = dicta[string] + int(num)
    else:
        dicta[string] = int(num)
print(*list(map(lambda x: x+' '+str(dicta[x]), dicta.keys())), sep="\n")


#from collections import OrderedDict
#d = OrderedDict()
#for _ in range(int(input())):
#    item, space, quantity = input().rpartition(' ')
#    d[item] = d.get(item, 0) + int(quantity)
#for item, quantity in d.items():
#    print(item, quantity)