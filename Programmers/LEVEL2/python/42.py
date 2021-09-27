# [(2018 KAKAO BLIND RECRUITMENT) [1차] 뉴스 클러스터링]
from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    info1 = []
    info2 = []
        
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            info1.append(str1[i]+str1[i+1])
    
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            info2.append(str2[i]+str2[i+1])
    
    Counter1 = Counter(info1)
    Counter2 = Counter(info2)
    
    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)