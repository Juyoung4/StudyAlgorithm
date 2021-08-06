# 표 편집
# 효율성 10개 중 4개 통과 못함
def up(start, end, x, check):
    for idx in range(start, end, -1):
        if check[idx] == 'O' : 
            x -= 1
            if not x : return idx
    return start+1

def down(start, end, x, check):
    for idx in range(start, end):
        if check[idx] == 'O' : 
            x -= 1
            if not x : return idx
    return end-1
        
def solution(n, k, cmd):
    stack = []
    check = ['O']*n
    
    start, end = 0, n-1
    
    for c in cmd:
        if c[0] == 'U': # 위로 업
            _, x = c.split()
            k = up(k-1, start-1, int(x), check)
        elif c[0] == 'D':
            _, x = c.split()
            k = down(k+1, end+1, int(x), check)
        elif c[0] == 'C':
            stack.append(k)
            check[k] = 'X'
            if k == end:
                k = up(k-1, start-1, 1, check)
                end = k
            elif k == start:
                k = down(k+1, end+1, 1, check)
                start = k
            else:
                k = down(k+1, end+1, 1, check)
        else:
            reset = stack.pop()
            check[reset] = 'O'
            if reset > end: end = reset
            if reset < start: start = reset
    return "".join(check)

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))