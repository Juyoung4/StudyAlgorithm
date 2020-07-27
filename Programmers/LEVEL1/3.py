# 평균 구하기
def solution(arr):
    return sum(arr)/len(arr)

# 📃만약 arr가 비었다면에 대한 코드 부족
def solution2(arr):
    return sum(arr)/len(arr) if arr else False

print(solution2([]))

