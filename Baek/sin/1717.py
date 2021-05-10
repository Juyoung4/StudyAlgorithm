# https://www.acmicpc.net/problem/1717
# 집합의 표현

def FindParent(parent, x):
    if parent[x] != x:
        parent[x]= FindParent(parent, parent[x])
    return parent[x]

# 3. 합집합 연산으로 같은 부모를 같도록 만든다.
def UnionParent(parent, a, b):
    a = FindParent(parent, a)
    b = FindParent(parent, b)
    if a != b: parent[b] = a
    # if a > b:
    #     parent[a] = b
    # else:
    #     parent[b] = a

if __name__ == "__main__":
    n, m = map(int, input().split())

    # 부모 => 일단 자기자신으로 만든다
    parents = [i for i in range(n+1)]

    # 출력은 1 a b 나왔을때 결과
    # m은 연산의 개수
    for _ in range(m):
        a, b, c = map(int, input().split())
        if a == 0: # 합집합 => union해준다.
            UnionParent(parents, b, c)
        else: # 두 원소가 같은 집합에 속하는지 => 부모가 같은지 확인
            if FindParent(parents, b) == FindParent(parents, c):
                print("YES")
            else:
                print("NO")

"""
초기에 {0}, {1}, {2}, ... {n} : n+1개 집합 이룸
합집합 연산 / 두 원소가 같은 집합에 포함되어 있는지 확인 연산
"""