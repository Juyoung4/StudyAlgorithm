s = input()
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
    print(len(result))
    print(result)