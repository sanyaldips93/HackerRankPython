
response_list = []
for i in range(int(input())):
    _ = int(input())
    num_list = list(map(int, input().split()))
    length_num_list = len(num_list)
    j = 0
    while j < length_num_list:
        if length_num_list == 1:
            response_list.append('Yes')
            j = 1
        elif num_list[j] >= num_list[j+1] and num_list[j] >= num_list[-1]:
            num_list.remove(num_list[j])
            num_list.reverse()
            length_num_list = len(num_list)
        else:
            response_list.append('No')
            break

print(*response_list, sep='\n')

# Correct Solution

#
# for i in range(int(input())):
#     _ = int(input())
#     num_list = list(map(int, input().split()))
#     j = 0
#     while j < (len(num_list)-1) and num_list[j] >= num_list[j+1]:
#         j = j+1
#     while j < (len(num_list)-1) and num_list[j] <= num_list[j+1]:
#         j = j+1
#     if j == (len(num_list)-1): print('Yes')
#     else: print('No')