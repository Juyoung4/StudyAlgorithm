# 가장 큰 수
# 순열 사용시 타임 오버
def solution(numbers):
    from itertools import permutations
    numbers = permutations(list(map(str, numbers)), len(numbers))
    numbers = map(lambda x : "".join(x), numbers)
    return max(numbers)

# 람다 function을 이용해서 풀이
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x*3, reverse=True)
    # str int는 '0000' 같은 걸 '0'으로 바꾸기 위해서 작성
    return str(int("".join(numbers)))

# 다른 사람 풀이
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

print(solution([6, 10, 2]))

