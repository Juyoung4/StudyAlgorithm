s = input()

def make_run_encoding(s):
    t, c = s[0], 1
    result = ''
    for i in s[1:]:
        if i == t:
            c += 1
        else:
            result += t + str(c)
            t, c = i, 1
    else:
        result += t+str(c)
    return result

result_ = 2
for i in range(1,len(s)):
    temp = make_run_encoding(s)
    if i == 1: result_ = len(temp)
    else:
        if len(temp) < result_:
            result_ = len(temp)
    s = s[-1] + s[:-1]
print(result_)
    