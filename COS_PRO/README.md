## 💡 COS PRO 외워가면 좋은 코드들

1. 소수 계산하기
``` python
n = 1000
checks = [False]*(n+1)
m = int(n**0.5)

for i in range(2, m+1):
    if not checks[i]: # False => 들린적이 없다!
        for j in range(i+i, n+1, i): # i배수 모두 True로 변경
            checks[j] = True

=> prime은? [i for i in range(2, n+1) if not checks[i]]
```

2. 조합 구하기
    - 모듈 사용
    ``` python
    from itertools import combinations

    result = list(combinations(arr, k))
    ```
    - 다중 for문 사용
    ``` python
    # 이 경우는 3개를 구할때임 그래서 -2, -1 순

    arr_len = len(arr) # 만약 arr_len = 6

    for i in range(0, arr_len - 2) : # i: 0 ~ 3
		for j in range(i + 1, arr_len - 1) : # j: 1 ~ 4
			for k in range(j + 1, arr_len) : # k = 2 ~ 5
				if arr[i]+arr[j]+arr[k] == n:
					answer += 1
    ```
    - dfs로 구현
    ``` python
    
    def combi(count, last_num, visited, N, k):
        if count == k:
            for i in range(N):
                if visited[i]: print(i, end=" ")
            print()
            return
        
        for i in range(last_num, N):
            if not visited[i]:
                visited[i] = 1
                combi(count+1, i+1, visited, N, k)
                visited[i] = 0

    def solution():
        arr = [1, 2, 7, 10, 3]
        len_arr = len(arr)
        k=3

        result = combi(0, 0, [0]*len_arr, len_arr, k)
    ```

3. 순열 구하기
    - 모듈 사용
    ``` python
    from itertools import permutations

    result = list(permutations(arr, k))
    ```
    - 다중 for문 사용
     ``` python
    arr_len = len(arr)

    for i in range(arr_len):
        for j in range(arr_len):
            if i == j: continue
            for k in range(arr_len):
                if i == k or j == k : continue
                print(i, j, k)
    ```

    - dfs로 구현
    ``` python
    def per(count, visited, N, k, result = []):
        if count == k:
            print(result)
            return
        
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                result.append(i)
                per(count+1, visited, N, k, result)
                result.pop()
                visited[i] = 0

    def solution():
        arr = [1, 2, 7, 10, 3]
        len_arr = len(arr)
        k=3

        result = per(0, [0]*len_arr, len_arr, k)
    ```

4. re 사용법
    ```
    1. sub => re.sub('패턴', 바꿀문자, 스트링) => 패턴에 해당되는 부분만 남기는 것
        re.sub('[A-Za-z0-9가-힣]', '', string)

    2. compile + sub
        h = re.complie('패턴')
        result = h.sub('', string)
    
    3. 해당 부분을 지우기 
        re.sub(r'\d+', '', string) => \d+ 연속 숫자 지우기
    ```