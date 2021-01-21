import sys
s = input()
INT_MIN = -10000000
answer = INT_MIN
len_ = len(s)

def calculation(s, cur_v, alpha_dict):
    global answer
    if not s:
        answer = max(cur_v, answer)
        return
    if len(s) != len_ and s[1] in alpha_dict.keys() and alpha_dict[s[1]] != -1:
        if s[0] == '-':
            calculation(s[2:], cur_v-alpha_dict[s[1]], alpha_dict)
        elif s[0] == '+': 
            calculation(s[2:], cur_v+alpha_dict[s[1]], alpha_dict)
        else:
            calculation(s[2:], cur_v*alpha_dict[s[1]], alpha_dict)
    else:
        for i in range(1, 5):
            if len(s) == len_:
                alpha_dict[s[0]] = i
                calculation(s[1:], i, alpha_dict)
            else:
                alpha_dict[s[1]] = i
                if s[0] == '-':
                    calculation(s[2:], cur_v-i, alpha_dict)
                elif s[0] == '+': 
                    calculation(s[2:], cur_v+i, alpha_dict)
                else:
                    calculation(s[2:], cur_v*i, alpha_dict)
                alpha_dict[s[1]] = -1
            

calculation(s, 0, {})
print(answer)