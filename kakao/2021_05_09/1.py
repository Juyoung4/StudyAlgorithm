def solution(s):
    answer = ''
    words = ['zero', 'one', 'two','three', 'four', 'five','six', 'seven', 'eight', 'nine']
    start = 0
    len_s = len(s)
    for idx in range(len_s):
        if s[idx].isdigit():
            answer += s[idx]
        else:
            if start < 2: start += 1
            else:
                temp = s[idx-start:idx+1]
                if temp in words:
                    answer += str(words.index(temp))
                    start = 0
                else:
                    start += 1
    print(answer)
    return int(answer)

"""
일부 자리수 영단어로 바꿔서 줌 => 프로도는 원래 숫자 찾기
"""