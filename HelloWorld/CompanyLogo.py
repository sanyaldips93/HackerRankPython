from collections import OrderedDict, Counter

# company_name = list(input())
# storage = OrderedDict()
#
# for i in range(len(company_name)):
#     storage.setdefault(company_name[i], 0)
#     storage[company_name[i]] += 1
#
# storage_sorted = OrderedDict(sorted(storage.items(), key=lambda x: (-x[1],x[0])))
#
# print(*storage_sorted.popitem(last=False), sep=' ')
# print(*storage_sorted.popitem(last=False), sep=' ')
# print(*storage_sorted.popitem(last=False), sep=' ')

# Using Counter

[print(*c) for c in Counter(sorted(input())).most_common(3)]
