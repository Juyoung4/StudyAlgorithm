# 구명보트
def solution(people, limit):
    answer = 0
    people.sort()
    if people[0] > limit: return 0
    len_p = len(people)
    left, right = 0, len_p-1
    while left <= right:
        if people[left] + people[right] <= limit:
            answer += 1
            left += 1
            right -= 1
        else: 
            answer += 1
            right -=1
    return answer