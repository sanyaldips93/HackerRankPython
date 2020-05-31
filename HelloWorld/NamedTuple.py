from collections import namedtuple

total_num_stu = int(input())
Students = namedtuple('Students', input().split())
list_tuples = []
sum = 0

for i in range(total_num_stu):
    list_tuples.append(Students(*input().split()))
    sum = sum + int(list_tuples[i].MARKS)

print('%.2f'%sum/total_num_stu)