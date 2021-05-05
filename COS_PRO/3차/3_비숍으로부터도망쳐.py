# 비숍으로부터 도망쳐
def solution(bishops):
	answer = 64
	rr = ["A", "B", "C", "D", "E", "F", "G", "H"] # 인덱스-비숍 위치(열 부분)
	cc = ["8", "7", "6", "5", "4", "3", "2", "1"]
	dirs = [(-1, -1),(-1, 1), (1, -1), (1, 1)] # 대각선의 방향
	boards = [[0 for _ in range(8)] for _ in range(8)]
	for b in bishops:
		r, c = cc.index(b[1]), rr.index(b[0])
		if not boards[r][c]:
			answer -= 1
			boards[r][c] = 1
		for x, y in dirs:
			nr, nc = r+x, c+y
			while 0 <= nr < 8 and 0 <= nc < 8:
				if not boards[nr][nc]:
					answer -= 1
					boards[nr][nc] = 1
				nr += x
				nc += y

	return answer

bishops1 = ["D5"]
ret1 = solution(bishops1)

print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

print("solution 함수의 반환 값은", ret2, "입니다.")