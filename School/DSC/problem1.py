# 스페인 알파벳

"""
스페인어 -> 확장 문자
메일의 최대 글자수 제한을 넘지 않기 위해 스페인 알파벳의 문자 갯수 센다
    => 예를 들어, espan~afu,tbol은 españafútbol로 총 12문자이다.

[입력]
espan~afu,tbol

[출력]
12
"""

def solution(st):
    count, idx= 0, len(st)-1
    while idx >= 0:
        if st[idx] in (',', '~') and st[idx-1].isalpha():
            idx -=1
        elif st[idx] == '..' and st[idx-2].isalpha():
            idx -= 2
        count += 1
        idx -=1
    return count
    
if __name__ == "__main__":
    print(solution(input()))