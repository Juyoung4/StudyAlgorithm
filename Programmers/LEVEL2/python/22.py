# 행렬의 곱셈
def solution(arr1, arr2):
    row, col = len(arr1), len(arr2[0])
    answer = [[0 for _ in range(col)] for _ in range(row)]
    arr2 = list(zip(*arr2))

    for r in range(row):
        for c in range(col):
            answer[r][c] += sum([i*j for i, j in zip(arr1[r], arr2[c])])
    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))