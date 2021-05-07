### SQL 문법

### SQL은 == 아님!!! "=" 하나만 쓰기 !!!
### 컬럼명 COUNT(ASD) 하면 AS "COUNT"로 바꾸기!!

1. ORDER BY : 순서
    ASC => 오름차순
    DESC => 내림차순
    ``` sql
        # 이런 경우 컬럼명1 기준으로 먼저 SORT후 컬럼명2기준으로 정렬
        ORDER BY 컬러명1 ASC, 컬럼명 DESC; 
        
        # 아래 처럼 수식을 써서 ORDER BY 가능!
        ORDER BY O.DATETIME - I.DATETIME DESC LIMIT 2;
    ```

2. 부속질의문
    * WHERE 문 사용
    ``` sql
        SELECT * FROM 테이블명 WHERE 컬러명1 = '123';

        SELECT * FROM 테이블명 WHERE 컬러명1 != '123'; # 같지 않는 경우

        SELECT * FROM 테이블명 WHERE 컬러명1 = (SELECT 컬럼명1 FROM 테이블명2 WHERE 컬럼명2 = 444);

        SELECT * FROM 테이블명 WHERE 컬러명1 IN (SELECT 컬럼명1 FROM 테이블명2 WHERE 컬럼명2 = 444);

        SELECT * FROM 테이블명 WHERE 컬러명1 > ALL/ANY/SOME (SELECT 컬럼명1 FROM 테이블명2 WHERE 컬럼명2 = 444);
    ```

3. LIMIT : 제한 두기
    * 출력 행수 제한 둘 수 있음
    ``` sql
        ~~~ LIMIT 행수;
    ```

4. 집계 함수
    * 집계 함수 : MAX, MIN, AVG, COUNT, SUM

5. IS NULL / IS NOT NULL / IFNULL
    * NULL 값인지 아닌지
     ``` sql
        ~~~ WHERE NAME IS NOT NULL;
        ~~~ WHERE NAME IS NULL;
    ```
    * IFNULL은 NULL을 반환할때 다른 값으로 출력할 수 있다.
    ``` sql
        SELECT IFNULL(컬럼명1, "NO NAME") FROM 테이블명;
    ```

6. AS 문법
    * 컬러명을 임의로 지정
    ``` sql
        SELECT NAME AS 'name!' FROM 테이블명;
    ```

7. GROUP BY / HAVING
    * GROUP BY : 원하는 그룹으로 묶어줌
    ``` sql
        SELECT ANIMAL_TYPE FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE ASC;
    ```
    * HAVING : 묶인 그룹에 대한 조건을 걸어줌
    ``` sql
        SELECT NAME, COUNT(NAME) FROM ANIMAL_INS GROUP BY NAME HAVING COUNT(NAME) > 1 ORDER BY NAME;

        # 이때 COUNT(NAME)의 컬럼며은 COUNT이다
        # COUNT(DISTINCT(NAME)) 이렇게 적으면 컬럼명은 COUNT(DISTINCT(NAME))으로 나오니 조심하기
    ```

8. 날짜 : MONTH, QUARTER, DAY / 시간 : HOUR, MINUTE, SECOND
    * YEAR, MONTH, DAY 하면 년, 월, 일만 가져올 수 있다
    * HOUR(DATIME) , MINUTE(DATETIME), SECOND(DATETIME) 하면 시, 분, 초만 가져올 수 있다
    ``` sql
        SELECT HOUR(DATETIME) AS 'HOUR', COUNT(HOUR(DATETIME)) AS 'COUNT' FROM ANIMAL_OUTS 
            GROUP BY HOUR(DATETIME) HAVING HOUR >= 9 AND HOUR <= 19 
                ORDER BY HOUR;
        
        # 이때 HAVING에는 HOUR을 넘겨줘야 한다
    ```

9. JOIN / OUTER JOIN
    * OUTER JOIN : A, B테이블이 있을때 B에 없는데 A에는 있으면 NULL로 채워짐
    * JOIN : A, B테이블 둘다 있는 것만 합쳐짐
    1. INNER JOIN = JOIN
    ``` sql
        SELECT gg.id, gg.name, s.title
             FROM GIRL AS gg JOIN SONG AS s 
                ON gg.id == s.id;

        SELECT GIRL.id, GIRL.name, SONG.title
            FROM GIRL JOIN SONG USING(id) 
                WHERE GIRL.cno == 413;
    ```

    2. OUTER JOIN => LEFT, RIGHT
    ``` sql
        # LEFT => SONG에 NULL값
        SELECT GIRL.id, GIRL.name, SONG.title
            FROM GIRL LEFT OUTER JOIN SONG 
                ON GIRL.id == SONG.id;

        # RIGHT => GIRL에 NULL값
        SELECT GIRL.id, GIRL.name, SONG.title
            FROM GIRL RIGHT OUTER JOIN SONG 
                ON GIRL.id == SONG.id;
    ```

10. LIKE 문법 / String
    * LIKE => 대소문자 구별안하고 EL, eL, El, el 모두 el로 취급
    ``` sql
        # PAK% => %는 PAK으로 시작하는 문자가 안에 있는지 확인
        SELECT ID, NAME FROM A WHERE NAME LIKE 'PAK%'

        SELECT ID, NAME FROM A WHERE NAME LIKE 'S_ _'; # S로 시작하는 3글자가 있는지 확인
        SELECT ID, NAME FROM A WHERE NAME LIKE '_ _S'; # S로 끝나는 3글자가 있는지 확인
    ```

11. IN 리스트 안에 있는지 확인
    ``` sql
        WHERE NAME IN ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty") 
    ```

12. CASE ~ WHEN ~ THEN ~ ELSE END
    ``` sql
        CASE
            WHEN 조건 절
            THEN 참일 경우 출력 내용
            ELSE 거짓일 경우 출력 내용
        END 
    ```