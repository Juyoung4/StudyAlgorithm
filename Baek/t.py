check = 0

def per(k, m, visited):
    global check
    if len(visited) == k:
        print(visited)
        return 

    for i in range(1, k+1):
        if i not in visited:
            visited.append(i)
            per(k, m, visited)
            visited.pop()

def solution(k, m):
    for i in range(1, k+1):
        per(k, m, [i])

print(solution(3, 2))
