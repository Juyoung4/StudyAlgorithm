# https://www.acmicpc.net/problem/3584
# 가장 가까운 공통 조상

from collections import deque

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        N = int(input())
        graph = [0 for _ in range(N+1)]
        for _ in range(N-1):
            a, b = map(int, input().split())
            graph[b] = a # 자식 정보에는 부모 정보만 넣기
        n1, n2 = map(int, input().split())
        
        n1_parents = deque([n1])
        while graph[n1]:
            n1_parents.append(graph[n1])
            n1 = graph[n1]
        
        n2_parents = deque([n2])
        while graph[n2]:
            n2_parents.append(graph[n2])
            n2 = graph[n2]
        
        len_p1, len_p2 = len(n1_parents), len(n2_parents)
        while n1_parents[len_p1-1]==n2_parents[len_p2-1]:
            len_p1-=1
            len_p2-=1
        print(n1_parents[len_p1])

"""
공통 조상 => 두 노드를 모두 자손으로 가지면서 깊이가 가장 깊은 노드
(즉 두 노드에 가장 가까운 노드)
"""