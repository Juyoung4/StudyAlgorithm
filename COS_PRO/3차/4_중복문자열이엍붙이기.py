# 중복 문자열 ㅇ이어붙이기
def solution(s1, s2):
	len_s1, len_s2 = len(s1), len(s2)
	len_ = abs(len_s1-len_s2)
	# s1 - s2
	answer = 0
	
	for i in range(len_s1-1, len_-1, -1):
		temp = s1[i:]
		len_t = len(temp)
		if temp == s2[:len_t]: answer = len_s1+len_s2 - len_t
			
	return answer


s1 = "ababc"
s2 = "abcdab"
ret = solution(s1, s2)

print("solution 함수의 반환 값은", ret, "입니다.")