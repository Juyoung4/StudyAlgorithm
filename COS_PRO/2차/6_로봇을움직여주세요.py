# 로봇을 움직여주세요
def solution(commands):
	answer = [0, 0]
	for c in commands:
		if c == "U": answer[1] += 1
		elif c == "D": answer[1] -= 1
		elif c == "R": answer[0] += 1
		else: answer[0] -= 1
	return answer

commands = "URDDL"
ret = solution(commands)

print("solution 함수의 반환 값은", ret, "입니다.")