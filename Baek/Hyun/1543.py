# 문서 검색
result = 0
def dfs(sN, s, tN, t, idx, count):
    global result
    if idx+tN > sN:
        result = max(result, count)
        return 
    
    if s[idx:idx+tN] == t:
        dfs(sN, s, tN, t, idx+tN, count+1)
    else:
        for i in range(idx+1, sN):
            if s[i] == t[0]: break
        else:
            result = max(result, count)
            return
        
        dfs(sN, s, tN, t, i, count)

if __name__ == "__main__":
    string = input()
    target = input()

    len_s, len_t = len(string), len(target)
    dfs(len_s, string, len_t, target, 0, 0)

    print(result)

