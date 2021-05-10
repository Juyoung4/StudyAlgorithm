# https://www.acmicpc.net/problem/10814
# 나이순 정렬

if __name__ == "__main__":
    N = int(input())
    members = []
    for i in range(N):
        a, b = input().split()
        members.append((int(a), b))

    members = sorted(members, key = lambda x: x[0])
    
    for date, name in members:
        print(date, name)

"""
나이가 같으면 먼저 가입 한 순 => 
회원 나이 증가 순 => 오름 차순
"""
