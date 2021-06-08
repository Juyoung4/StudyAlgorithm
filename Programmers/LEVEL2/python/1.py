#[전화번호 목록]
def solution(phone_book):
    if not 1 <= len(phone_book) <= 1000000: return False
    if len(phone_book)==1: return True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]: return False
        else: pass
    return True

# 다른 사람 풀이 -> sort없이 구현 한것 위코드 보다 빠름! -> 효율성 좋음
def solution(phone_book):
    for i in range(len(phone_book)):
        pivot = phone_book[i]
        for j in range(i+1, len(phone_book)):
            strlen = min(len(pivot), len(phone_book[j]))
            if pivot[:strlen] == phone_book[j][:strlen]:
                return False
    return True

# 기본적인 해쉬 구조를 이용해서 풀어도 가능


