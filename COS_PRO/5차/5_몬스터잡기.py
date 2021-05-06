# 몬스터잡기
def solution(enemies, armies):
	answer = 0
	enemies.sort()
	# 내 공격력 >= 몬스터 공격력 : 이김
	idx = 0
	len_e = len(enemies)
	for a in armies:
		if a >= enemies[idx]:
			answer += 1
			if idx + 1 >= len_e: break
			else: idx += 1
	return answer

enemies1 = [1, 4, 3]
armies1 = [1, 3]
ret1 = solution(enemies1, armies1)

print("solution 함수의 반환 값은", ret1, "입니다.")

enemies2 = [1, 1, 1]
armies2 = [1, 2, 3, 4]
ret2 = solution(enemies2, armies2)

print("solution 함수의 반환 값은", ret2, "입니다.")