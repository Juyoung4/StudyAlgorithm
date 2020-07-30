#2019 카카오 개발자 겨울 인턴십 크레인 인형뽑기 게임
def solution(board, moves):
    bucket=[-1]
    answer=0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]:
                if bucket[-1] == board[j][i-1]:
                    answer += 1
                    del bucket[-1]
                else:
                    bucket.append(board[j][i-1])
                board[j][i-1] = 0
                break
    return answer*2
    