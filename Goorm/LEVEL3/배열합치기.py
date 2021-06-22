# https://level.goorm.io/exam/43250/%EB%B0%B0%EC%97%B4-%ED%95%A9%EC%B9%98%EA%B8%B0/quiz/1

n, m = map(int, input().split())
user_input = list(map(int, input().split())) + list(map(int, input().split()))
user_input.sort()
for n in user_input:
	print(n, end=" ")