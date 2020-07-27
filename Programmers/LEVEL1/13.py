# 문자열 내 마음대로 정렬하기
"""
python lambda 사용하기

lambda 인자 : 표현식

def inc(n):
	return lambda x: x + n

* lambda를 이용해서 정렬 사용하기
c = sorted(a, key = lambda x : x[0])
sorted(리스트, key = 함수)
=> key에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬한다
=> 여기서는 아이템 0번째 index를 기준으로 오름차순으로 정렬

sorted(e, key = lambda x : (x[0], -x[1]))
=> 첫번째로 0번째 인덱스 기준으로 오름차순 정렬 -> 그 안에서 1번째 인덱스 기준으로 내림차순 정렬

**
sorted(리스트, key=lambda parameter_list: expression)
"""
def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n],x))
