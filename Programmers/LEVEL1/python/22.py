#자연수 뒤집어 배열로 만들기
def solution(n):
    return list(map(int,str(n)[::-1]))

"""
python의 map을 잘 이용하기
map(함수, 대상)
"""

#다른 사람 코드
def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]
