# 같은 숫자는 싫어
def solution(arr):
    return [arr[0]]+[arr[i] for i in range(1,len(arr)) if arr[i-1] != arr[i]]

# 다른 사람  코드
def no_continuous(s):
    # 함수를 완성하세요
    a=[ v for i,v in enumerate(s) if s[i-1]!=s[i]]

    return a

# enumerate사용해서 인덱스와 값 한방에 사용..천재댜유ㅠㅠㅠ