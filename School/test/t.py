# 1. 병원 m개 선택 (모든 병원의 조합을 구한다)
# 2. 각 사람들이 선택된 병원까지 갈 수 있는 최소를 구함.
# 3. 1,2를 통해 구해진 모든 경우의 최소를 구함.
# 필요한것? 병원의 좌표.
# 필요한 함수? 그 병원이 선택된 병원인지 확인해야함.    -> 필요없음 선택된 순간에 사람들과의 거리를 구하기 때문
## -> 모든 병원의 경우의 수만큼 루프 순회해야함. 
##-> 최악의 경우 13Combination6만큼 순회해야함 + 회당 n*n번 table을 확인해야하니->
## 대충 10^6*50*50 ~= 10^8 * 25. 1억이 1초니까, 최악의 경우 1초가 넘게 걸릴 수 있음. -> 어? 아닌가? 아닐것같음.

# 일단은 진행 ok

from collections import deque
import sys
N,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
hospitals=deque()
people=deque()
p_hos=deque()

# 사람들에 해당하는 좌표와,  병원들에 해당하는 좌표를 저장
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            hospitals.append((i,j))
        if board[i][j] == 1:
            people.append((i,j))
print(hospitals)
print(people)
print()
#병원 조합을 만들기 위한 visited list
visited = [False for _ in range(len(hospitals))]

def calcLength(t1, t2):
    return abs(t1[0]-t2[0]) + abs(t1[1]-t2[1])

answer = sys.maxsize

def findCombination(n):
    global answer
    print(p_hos)
    if len(p_hos) == m:
        #병원이 m개 선택되는 순간
        total_sum = 0
        for person in people:
            dist=sys.maxsize
            for hospital in p_hos:
                dist = min(dist, calcLength(person,hospital))
            total_sum += dist
        answer = min(answer, total_sum)
        return
    
    if n == N:
        # 순회를 끝까지 갔을 경우
        return
    for i in range(n,len(hospitals)):
        if not visited[i]:
            p_hos.append(hospitals[i])
            visited[i] = True
            findCombination(i)
            p_hos.pop()
            visited[i] = False

findCombination(0)
# 아 뭔가 케이스 6번이 answer에 maxsize들어가서 그런것 같은데 반례를 못찾겠네..............
print(answer)