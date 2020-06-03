

a,b = list(map(int, input().split()))
marks_subjects = []
for i in range(b):
    marks_subjects.append(list(map(float, input().split())))

zip_list = [*zip(*marks_subjects)]
for j in range(a):
    print(sum(zip_list[j])/len(zip_list[j]))

