# 네트워크
def find_parent(networks, node):
    if networks[node] != node : # 자기 자신이 아니면 -> parent가 아님
        return find_parent(networks, networks[node])
    return networks[node]

def union_parent(a, b, networks):
    A_parent = find_parent(networks, a)
    B_parent = find_parent(networks, b)
    
    if A_parent != B_parent:
        if A_parent > B_parent:
            networks[b] = a
        else:
            networks[a] = b
    
    return networks

def solution(n, computers):
    answer = 0
    if n == 1: return 1
    networks = [i for i in range(n)]
    
    computers_temp = []
    
    for idx1, com in enumerate(computers):
        for idx2, node in enumerate(com):
            if idx1==idx2: continue
            if com[idx2] == 1 and [idx2, idx1] not in computers_temp:
                computers_temp.append([idx1, idx2])
    print(computers_temp)
    print(networks)
    for a, b in computers_temp:
        print("edge : ", (a, b))
        networks = union_parent(a, b, networks)
        print("update : ", networks)
    
    print(networks)
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))