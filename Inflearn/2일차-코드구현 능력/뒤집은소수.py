# N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램 작성


"""
[INPUT]
32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력한다.
단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
[OUTPUT]
첫 줄에 뒤집은 소수를 출력합니다. 출력순서는 입력된 순서대로 출력합니다.

[INPUT EX]
5
32 55 62 3700 250

[OUTPUT EX]
23 73
"""
def isPrime(num):
    if num == 1: return False
    for i in range(2, int(num**0.5)+1):
        if not num % i: return False
    return True
        

def solution(len_):
    nums = input().split()
    if len_ != len(nums) : return -1
    result = []
    for num in nums:
        temp = int(num[::-1])
        if isPrime(temp): result.append(temp)
    return result
    
if __name__ == "__main__":
    print(solution(int(input())))
