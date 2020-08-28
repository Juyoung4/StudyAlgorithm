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

        
    

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "headgear"], ["green_turban", "eyewear"],["crow_mask", "face"]]))