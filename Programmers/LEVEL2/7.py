# 타켓 넘버

result = 0
def dfs(cur_num, numbers, len_n, target, visited):
    global result
    if cur_num == len_n:
        temp = 0
        for i, j in zip(visited, numbers):
            temp += i*j
        if target == temp: result += 1
        return
    
    visited[cur_num] = 1
    dfs(cur_num+1, numbers, len_n, target, visited)
    visited[cur_num] = -1
    dfs(cur_num+1, numbers, len_n, target, visited)
        
def solution(numbers, target):
    len_n = len(numbers)
    dfs(0, numbers, len_n, target, [0]*len_n)
    return result

"""다른 사람 풀이
[1]
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer

[2]
def dfs(nums, i, n, t):
    ret = 0
    if i==len(nums):
        if n==t: return 1
        else: return 0
    ret += dfs(nums, i+1, n+nums[i], t)
    ret += dfs(nums, i+1, n-nums[i], t)
    return ret

def solution(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer
"""
