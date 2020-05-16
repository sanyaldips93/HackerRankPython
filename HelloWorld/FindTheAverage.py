if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

# print(student_marks)
scores = 0
if query_name in student_marks.keys():
    list_val = student_marks.get(query_name)
    for score in list_val:
        scores = scores + score
    avg_scores = scores/3
    print(f'{avg_scores:.2f}')
