#  종이접기
def solution(grid):
    answer = 0
    for i in range(4):
        for j in range(4):
            print("(i, j) : ", (i, j))
            for k in range(j + 1, 4, 2):
                print("k : ", k)
                print("check : ", (i, j), (i, k), " #### ", (j, i), (k, i))
                answer = max(answer, max(grid[i][j] + grid[i][k], grid[j][i] + grid[k][i]))
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
grid = [[1, 4, 16, 1], [20, 5, 15, 8], [6, 13, 36, 14], [20, 7, 19, 15]]
ret = solution(grid)
print(ret)