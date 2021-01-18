# 최솟 값과 그 갯수를 출력하기
# min, count함수 사용시 runtime error

N = int(input())
a = list(map(int, input().split()))
INT_MIN = a[0]
count = 0
for i in a:
    if INT_MIN == i:
        count += 1
    if INT_MIN > i:
        count = 1
        INT_MIN = i
print(INT_MIN, count)