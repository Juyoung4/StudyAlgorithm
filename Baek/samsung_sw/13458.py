# 시험 감독
# https://www.acmicpc.net/problem/13458
import sys


def exam():
    total_teacher = 0
    for people in peoples:
        t = people - B
        if t <= 0: total_teacher += 1
        else:
            n, m = t//C, t%C
            if m:
                total_teacher += (n+2)
            else:
                total_teacher += n+1
    return total_teacher



if __name__ == "__main__":
    N = int(sys.stdin.readline())
    peoples = list(map(int, sys.stdin.readline().split()))
    B, C = map(int, sys.stdin.readline().split())

    print(exam())