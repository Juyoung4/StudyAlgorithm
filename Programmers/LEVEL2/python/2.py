#위장
def solution(clothes):
    closet={}
    result = 1
    for i in clothes:
        if not i[1] in closet.keys():
            closet[i[1]] = 1
            continue
        else:
            closet[i[1]] += 1
            continue
    for i in closet.values():
        result *= i + 1
    return result - 1


### 다른 사람 풀이
import collections
from functools import reduce

def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1
    
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "headgear"], ["green_turban", "eyewear"],["crow_mask", "face"]]))

