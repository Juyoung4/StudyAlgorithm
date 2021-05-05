# 다음과 같이 import를 사용할 수 있습니다.
# import math

from collections import deque
def solution(garden):
    flowers = deque()
    len_g = len(garden)
    len_gg = len_g**2
    for i in range(len_g):
        for j in range(len_g):
            if garden[i][j]: flowers.append((i, j, 0))
    if len(flowers) == len_gg: return 0
    else:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while flowers:
            r, c, y = flowers.popleft()
            for i in range(4):
                nr, nc = r+dirs[i][0], c+dirs[i][1]
                if 0 <= nr < len_g and 0 <= nc < len_g and not garden[nr][nc]:
                    garden[nr][nc] = 1
                    flowers.append((nr, nc, y+1))
    return y

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

# garden2 = [[1, 1], [1, 1]]
# ret2 = solution(garden2)

# # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은", ret2, "입니다.")