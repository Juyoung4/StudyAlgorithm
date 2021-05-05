# 언제까지 오르막길이야?!
def solution(arr):
    len_a = len(arr)
    max_up, up = 0, 0
    for i in range(len_a-1):
        if arr[i] < arr[i+1]: 
            up += 1
        else:
            max_up = max(max_up, up)
            up = 0
    return max_up + 1


arr1 = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
arr2 = [3, 1, 1, 4, 1, 1, 2, 2, 2, 4]
arr3 = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
ret = solution(arr2)

print("solution 함수의 반환 값은", ret, "입니다.")