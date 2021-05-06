#2016년
"""
datetime 모듈 사용하기
from datetime import date

[1] 요일 출력하기 : day[date(year, month, day).weekday()]
"""
from datetime import date
def solution(a, b):
    answer = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    return answer[date(2016,a,b).weekday()]