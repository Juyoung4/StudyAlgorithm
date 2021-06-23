# 큰수 만들기
def solution(number, k):
    stack = []
    for idx, num in enumerate(number):
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        if k == 0: # 다 뺐으니까 나머지 다 넣어주기
            stack.extend([n for n in number[idx:]])
            break
        stack.append(num)
        
    stack = (stack[:-k] if k > 0 else stack)
    
    return "".join(stack)

print(solution("1002", 2))