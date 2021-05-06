# 그래프에서 싸이클 찾기
def find(parent, u):
	if u == parent[u]:
		return u
	parent[u] = 0
	return parent[u]

def merge(parent, u, v):
	u = find(parent, u)
	v = find(parent, v)
	if u == v:
		return True
	
	return False

def solution(n, connections):
	answer = 0
	parent = [0]+[c[0] for c in connections]
	for i, connection in enumerate(connections):
		if merge(parent, connection[0], connection[1]):
			answer = i + 1
			break
	return answer

n = 3
connections = [[1, 2], [1, 3], [2, 3]]
ret = solution(n, connections)

print("solution 함수의 반환 값은", ret, "입니다.")