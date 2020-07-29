#예산
"""
알고리즘때 내가 최대로 일할 수 있는 시간 구하는 것과 비슷
    =>그리드 사용했던거 같운데...

개수가 많아야되는게 뽀인뜨=>가장 적은 돈을 먼저 선택한 결과가 가장 좋을 거 같음
"""
# def solution(d, budget):
#     count=0
#     while True:
#         if d and budget - min(d)>=0:
#             budget -= min(d)
#             d.remove(min(d))
#             count += 1
#         else: break
#     return count

def solution(d, budget):
    count=0
    while not budget < 0:
        if not d: 
            count+=1
            break
        budget -= min(d)
        d.remove(min(d))
        count += 1
    return count-1

## 두개 다 작성한건데 2번째 코드가 더 빠름
print(solution([1,3,2,5,4],9))