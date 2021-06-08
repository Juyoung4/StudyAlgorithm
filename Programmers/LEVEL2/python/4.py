# 프린터
def solution(priorities, location):
    idx = [i for i in range(len(priorities))]
    count = 0
    while True:
        max_ = priorities.index(max(priorities))
        if idx[max_] == location:
            count += 1
            break
        #print("not change: ",priorities,idx)
        if not max_:
            priorities.pop(max_)
            idx.pop(max_)
            count += 1
        else:
            priorities.append(priorities.pop(0))
            idx.append(idx.pop(0))
        #print("change : ",priorities,idx)
        #print("count :", count)
    return count