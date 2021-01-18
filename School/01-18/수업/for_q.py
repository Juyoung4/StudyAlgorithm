# 규칙적인 19단 구구단 출력

for i in range(1,20):
    for j in range(1,20):
        if j % 2 and j != 19:
            print("{0} * {1} = {2}".format(i,j, i*j), end=" / ")
        else:
            print("{0} * {1} = {2}".format(i,j, i*j))
 