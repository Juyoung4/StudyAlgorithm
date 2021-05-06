#제일 작은 수 제거하기
#del과 pop은 인덱스를 이용해서 값 제거 => del a[인덱스]
#remove는 값을 이용해서 제거 => a.remove(값)
def solution(arr):
    arr.remove(min(arr))
    return arr if arr else [-1]


