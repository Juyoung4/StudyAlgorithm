answer = [0, 0]

def check(arr, row_start, row_end, col_start, col_end):
    global answer
    temp = arr[row_start][col_start]

    for i in range(row_start, row_end):
        for j in range(col_start, col_end):
            # 모든 같은 숫자가 아니면 => false => split 후보
            if temp != arr[i][j]:
                return False
                
    answer[temp] += 1
    return True

def four_split(arr, row_start, row_end, col_start, col_end):
    # 만약, 4등분한 결과가 1이면 그냥 개수 세고 return
    if row_end - row_start == 1:
        answer[arr[row_start][col_start]] += 1
        answer[arr[row_start][col_end]] += 1
        answer[arr[row_end][col_start]] += 1
        answer[arr[row_end][col_end]] += 1
        return
    else: # 4등분을 해서 진행
        row_half = (row_end+row_start) // 2 # range(row_start, row_half), range(row_half, row_end-1)
        col_half = (col_end+col_start) // 2
        # 첫 번째
        if not check(arr, row_start, row_half, col_start, col_half):
            four_split(arr, row_start, row_half, col_start, col_half)
        # 두 번째
        if not check(arr, row_start, row_half, col_half, col_end):
            four_split(arr, row_start, row_half, col_half, col_end)
        # 세 번째
        if not check(arr, row_half, row_end, col_start, col_half):
            four_split(arr, row_half, row_end, col_start, col_half)
        # 네 번째
        if not check(arr, row_half, row_end, col_half, col_end):
            four_split(arr, row_half, row_end, col_half, col_end)

def solution(arr):
    global answer
    len_arr = len(arr)
    if len_arr == 1: 
        answer[arr[0]] += 1
        return answer
    
    if not check(arr, 0, len_arr, 0, len_arr): # 첫 번째 전체 확인
        four_split(arr, 0, len_arr, 0, len_arr)
        
    return answer