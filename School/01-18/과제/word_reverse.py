a = input()
b = input()
if len(a) > len(b): print("No")
else:
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))
    if a == b: print("Yes")
    else:
        print("No")