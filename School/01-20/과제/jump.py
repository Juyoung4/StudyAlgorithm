n = int(input())
steps = list(map(int, input().split()))
min_ = n+1
def jumps(cur_idx, cnt, check=None):
    global min_
    #print(cur_idx, cnt, check)
    if cur_idx == n-1:
        min_ = min(min_, cnt)
        return cnt

    for i in range(steps[cur_idx]):
        if cur_idx + (i+1) <= n-1:
            jumps(cur_idx+(i+1), cnt+1, i+1)
        else: continue

jumps(0, 0)
if n+1 == min_: print(-1)
else:
    print(min_)