#k번째 수
def solution(array, commands):
    return  [sorted(array[i[0]-1:i[1]])[i[2]-1] for i in commands]

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

#다른사람 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

#map함수를 이용하여 for문 대신 ㅈ사용...