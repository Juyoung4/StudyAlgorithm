# 없어진 기록 찾기

# 1. 부속 질의문
SELECT ANIMAL_ID, NAME FROM ANIMAL_OUTS 
    WHERE ANIMAL_ID NOT IN (SELECT ANIMAL_ID FROM ANIMAL_INS) 
        ORDER BY ANIMAL_ID ASC;

# 2. JOIN
SELECT outs.ANIMAL_ID, outs.NAME
    FROM ANIMAL_OUTS AS outs LEFT OUTER JOIN ANIMAL_INS AS ins
        ON outs.ANIMAL_ID = ins.ANIMAL_ID
            WHERE ins.ANIMAL_ID IS NULL
                ORDER BY ANIMAL_ID ASC;

"""
ANIMAL_INS : ANIMAL_ID(PK) [동물 보호소에 들어온 동물의 정보를 담은 테이블]
ANIMAL_OUTS : ANIMAL_ID(FK) [동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블]

천재지변으로 인해 일부 데이터가 유실되었습니다. 
입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 
ID 순으로 조회하는 SQL문을 작성해주세요.
"""