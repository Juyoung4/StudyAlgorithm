#행렬의 덧셈
def solution(arr1, arr2):
    return [[arr1[i][j]+arr2[i][j] for j in range(len(arr1[i]))] for i in range(len(arr1))]

# 다른 사람 풀이
def solution(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

#zip을 이용해서 하는 방법이 더 빠름 