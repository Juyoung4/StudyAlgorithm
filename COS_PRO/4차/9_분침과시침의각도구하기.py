def solution(hour, minute):
	# 시계는 360도
	# 시간은 0 ~ 59 으로 60개 -> 즉 1분에 6도 움직임
	
	hour = int(hour)*5 if hour != 12 else 0
	answer = abs(hour-minute)*6
	
	return "{:.1f}".format(answer)

hour = 3
minute = 0
ret = solution(hour, minute)

print("solution 함수의 반환 값은", ret, "입니다.")