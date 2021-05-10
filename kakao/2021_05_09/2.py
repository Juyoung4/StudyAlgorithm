def solution(places):
    answer = []
    dirs1 = [(0, -1), (-1, 0), (0, 1), (1, 0)] # 서 북 동 남
    dirs2 = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    ds = [(2, 3), (0, 3), (1, 0), (1, 2)]
    stop = False
    for place in places:
        stop = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    nots = [0]*4
                    for k in range(1, 3):
                        for p in range(4):
                            if nots[p] == 1: continue
                            r, c = i+dirs1[p][0]*k, j+dirs1[p][1]*k
                            if 0 <= r < 5 and 0 <= c < 5:
                                if place[r][c] == 'X': nots[p] = 1
                                elif place[r][c] == 'P':
                                    stop = True
                                    break
                        if stop: break
                    else: # 대각 선
                        for p in range(4):
                            r, c = i+dirs2[p][0], j+dirs2[p][1]
                            if 0 <= r < 5 and 0 <= c < 5:
                                if place[r][c] == 'P':
                                    one = (r+dirs1[ds[p][0]][0], c+dirs1[ds[p][0]][1])
                                    two = (r+dirs1[ds[p][1]][0], c+dirs1[ds[p][1]][1])
                                    if 0 <= one[0] < 5 and 0 <= one[1] < 5:
                                        if place[one[0]][one[1]] != 'X':
                                            stop = True
                                            break
                                    if 0 <= two[0] < 5 and 0 <= two[1] < 5:
                                        if place[two[0]][two[1]] != 'X':
                                            stop = True
                                            break
                    if stop: break
                if stop: break
            if stop: break

        if stop: answer.append(0)
        else: answer.append(1)                                      
    return answer