# 45. 2021 Dev-Matching 로또의 최고 순위와 최저 순위
def score(num):
    if num == 6: return 1
    elif num == 5: return 2
    elif num == 4: return 3
    elif num == 3: return 4
    elif num == 2: return 5
    else: return 6
    
def solution(lottos, win_nums):
    min_ = 0
    zero = 0
    for l in lottos:
        if l == 0: 
            zero += 1
            continue
        if l in win_nums: min_ += 1

    return [score(min_+zero), score(min_)]

"""
로또 : 1 ~ 45 숫자 중 6개 찍어서 맞춤
로또 순위
    [1] : 6개 번호 모두 일치
    [2] : 5개
    [3] : 4개
    [4] : 3개
    [5] : 2개
    [6] : 그 외

민우 : 최고 순위 + 최저 순위
(ex) [44, 1, 0, 0, 31 25] / 당청 : [31, 10, 45, 1, 6, 19]
최저 : 0을 뺐을때 받을 점수
최고 : 0을 포함한 받을 점수
"""

"""
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
"""