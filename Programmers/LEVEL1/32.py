#완주하지 못한 선수
"""
import collections
collection모듈 사용

print(collections.Counter(lst))
"""

import collections
def solution(participant, completion):
    participant= (collections.Counter(participant))
    for i in completion:
        if participant[i]:
            participant[i] -= 1
    return participant.most_common(1)[0][0]