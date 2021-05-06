def solution(a, b):
	answer = 0
	c = [0]*(b+1)
	for i in range(2, b+1):
		for j in range(2, i):
			if not i%j: break
		else:
			if a <= i**2 <= b or a <= i**3 <= b:
				if a <= i**2 <= b:
					answer += 1
				if a <= i**3 <= b:
					answer += 1
	return answer

a =  6
b =  30
ret = solution(a, b)

print("solution 함수의 반환 값은", ret, "입니다.")