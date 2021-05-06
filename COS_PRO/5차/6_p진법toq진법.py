# p진법 to q진법
def solution(s1, s2, p, q):
	answer = ''
	temp = int(s1, p) + int(s2, p)
	
	while temp != 0:
		answer += str(temp%q)
		temp //= q
	
	return answer[::-1]

s1 = "112001"
s2 = "12010"
p = 3
q = 8
ret = solution(s1, s2, p, q)

print("solution 함수의 반환 값은", ret, "입니다.")