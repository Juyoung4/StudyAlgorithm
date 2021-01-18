N = int(input())
students = [list(map(int, input().split())) + [i+1] for i in range(N)]
students.sort(key = lambda x: (-x[0], -x[1], x[2]))

for i in students:
    print(i[0], i[1], i[2])