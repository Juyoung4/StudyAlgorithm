# top_k 숫자 구하기

N, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
print(a[k-1])