s, n = input().split()
num = [int(input()) for i in range(int(n))]

for i in num:
    if i == 1:
        s = s[1:] + s[0]
        print(s)
    elif i == 2:
        s = s[-1] + s[:-1]
        print(s)
    else:
        s = s[::-1]
        print(s)
