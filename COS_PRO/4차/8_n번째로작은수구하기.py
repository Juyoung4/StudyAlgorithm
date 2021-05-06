from itertools import permutations
def solution(card, n):
	len_c = len(card)
	result = []
	for p in permutations(card, len_c):
		temp = ''
		for s in p:
			temp += str(s)
		temp = int(temp)
		if temp not in result: result.append(int(temp))
	result.sort()
	if n in result: return result.index(n)+1
	else: return -1

card1 = [1, 2, 1, 3]
n1 = 1312
ret1 = solution(card1, n1)

print("solution 함수의 반환 값은", ret1, "입니다.")

card2 = [1, 1, 1, 2]
n2 = 1122
ret2 = solution(card2, n2)

print("solution 함수의 반환 값은", ret2, "입니다.")