n = int(input())
student = []

for i in range(n):
    name, score = input().split()
    student.append([name, int(score)])

result = [[] for _ in range(100)]

for i in range(n):
    result[student[i][1]].append(student[i][0])

for i in range(100):
    if result[i]:
        for name in result[i]:
            print(result[i][0], end = ' ')