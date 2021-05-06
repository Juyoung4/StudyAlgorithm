# 43. 찾아라 프로그래밍 마에스터 폰켓몬
def solution(nums):
    temp_nums = set(nums)
    len_n = len(nums)//2
    len_t = len(temp_nums)
    if len_t >= len_n: return len_n
    else: return len_t

"""
연구실 총 N 마리 -> N/2가져가도 된다함
같은 종류 폰켓몬 = 같은 번호 가짐
가장 많은 종류의 폰켓몬을 선택하는 방법
"""

"""
다른 사람 풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
"""