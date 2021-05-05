# 합이 k배수가 되는 수

# 버전 1
answer = 0
def combi(count, last_num, visited, arr, K, N):
	global answer
	if count == 3:
		temp = 0
		for i in range(N):
			if visited[i]: temp += arr[i]
		if temp % K == 0: answer += 1
		return
	
	for i in range(last_num, N):
		if not visited[i]:
			visited[i] = 1
			combi(count+1, i ,visited, arr, K, N)
			visited[i] = 0

def solution(arr, K):
	len_a = len(arr)
	visited = [0]*len(arr)
	combi(0, 0, visited, arr, K, len_a)
	return answer

# 버전 2
from itertools import combinations

def solution2(arr, K):
    answer = 0
    for c in combinations(arr, 3):
        if sum(c) % K == 0: answer += 1
    return answer


arr = [1, 2, 3, 4, 5]
K = 3
ret = solution(arr, K)

print("solution 함수의 반환 값은", ret, "입니다.")