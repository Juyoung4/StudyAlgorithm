# 몇번 연산을 해야하나요
from collections import deque
max_ = 10001
def solution(number, target):
	queue = deque()
	queue.append((number, 0))
	visited=[0]*max_
	visited[number] = 0
	while queue:
		num, c = queue.popleft()
		if num == target:
			return c
		if num+1 < max_ and not visited[num+1]: # 더하기
			visited[num+1] = 1
			queue.append((num+1, c+1))
		if 0 <= num-1 < max_ and not visited[num-1]:
			visited[num-1] = 1
			queue.append((num-1, c+1))
		if 0 <= num*2 < max_ and not visited[num*2]:
			visited[num*2] = 1
			queue.append((num*2, c+1))

number1 = 5
target1 = 9
ret1 = solution(number1, target1)

print("solution 함수의 반환 값은", ret1, "입니다.")

number2 = 3
target2 = 11
ret2 = solution(number2, target2)

print("solution 함수의 반환 값은", ret2, "입니다.")