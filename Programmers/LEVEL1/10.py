# 서울에서 김서방 찾기
"""
format 메소드 사용

(ex-값 여러개 넣기)
'Hello, {0} {2} {1}'.format('Python', 'Script', 3.6)

(ex-같은 값 여러개 넣기)
'{0} {0} {1} {1}'.format('Python', 'Script')

(ex-인덱스 생략해서 넣기)
'Hello, {} {} {}'.format('Python', 'Script', 3.6)

(ex-변수 그대로 사용하기)
language = 'Python'
version = 3.6
f'Hello, {language} {version}'

(ex-문자열 정렬하기)
'{인덱스:<길이}'.format(값)
'{0:<10}'.format('python')
부등호 방향 < 왼쪽 => 왼쪽으로 정렬하고 남은 공간 공백

(ex-숫자 개수 맞추기)
'{0:08.2f}'.format(150.37) => 총길이 8자리, 2자리 소수점
'00150.37'

"""
def solution(seoul):
    return '김서방은 {}에 있다'.format(seoul.index("Kim"))