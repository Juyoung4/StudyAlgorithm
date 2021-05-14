# 3. 결정 알고리즘 - 뮤직 비디오
import time
"""

DVD - N개 곡 들어감 => 라이브에서의 순서 유지(즉, 1이랑 5 녹화하려면 1 ~ 5사이 노래도 녹화해야함)
M개의 DVD에 모든 동영상 녹화하기로 함 
이때 DVD의 크기를 최소로 하려 함
"""

def solution1(N, M, music):
    bound = sum(music) // M # 최솟값 바운더리 정해서 +1씩 증가하며 확인
    while True:
        count = 0
        temp_sum = 0
        for i in range(N):
            if temp_sum + music[i] <= bound:
                temp_sum += music[i]
            else:
                if count + 1 >= M:
                    bound += 1
                    break
                else:
                    count += 1
                    temp_sum = music[i]
        else:
            break
    return bound

def counts(music, len_):
    count = 1
    temp_sum = 0
    for m in music:
        if temp_sum + m > len_:
            count += 1
            temp_sum = m
        else:
            temp_sum += m
    return count

def solution2(N, M, music):
    maxs = max(music)
    start, end = 1, sum(music)
    result = 0
    while start <= end:
        mid = (start+end)//2
        if mid >= maxs and counts(music, mid) <= M:
            end = mid-1
            result = mid
        else:
            start = mid+1

    return result


if __name__ == "__main__":
    import sys
    sys.stdin=open("Inflearn/4일차/in5.txt", "r")

    N, M = map(int, input().split())
    
    music = list(map(int, input().split()))

    start_time = time.time()
    print(solution1(N, M, music))
    end_time = time.time()
    print("WorkingTime1: {} sec".format(end_time-start_time))

    start_time = time.time()
    print(solution2(N, M, music))
    end_time = time.time()
    print("WorkingTime2: {} sec".format(end_time-start_time))

    # 2번 방법이 더 빠름 2번 처럼 짜기 -> 그리디