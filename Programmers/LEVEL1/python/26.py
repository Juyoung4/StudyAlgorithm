#최대공약수와 최소공배수
"""
x=a*b
y=b*c이면
최대 공약수는 b이다. 
최소 공배수는 a*b*c이다
그러므로 최소 공배수= x*y // 최대공약수
"""
def solution(n, m):
    a=n*m
    while m != 0:
        n,m=m,n%m
    return [n,a//n]

print(solution(2,5))

#다른사람 풀이
def solution(n, m):
    gcd = lambda a,b : b if not a%b else gcd(b, a%b)
    lcm = lambda a,b : a*b//gcd(a,b)
    return [gcd(n, m), lcm(n, m)]