#올바른 괄호
def solution(s):
    answer = False
    
    stack = []
    
    for st in s:
        if st == ")":
            if not stack: 
                return False
            else:
                stack.pop()
        else:
            stack.append(st)
    
    if not stack: answer = True # return len(stack)) == 0 이렇게 해도 ㅗ딤
            
    return answer