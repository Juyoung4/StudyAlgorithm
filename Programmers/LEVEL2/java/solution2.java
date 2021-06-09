package Programmers.LEVEL2.java;
import java.util.*;

public class solution2 {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> closet = new HashMap<String, Integer>();
        //closet 옷넣기
        for (int i = 0; i < clothes.length; i++) { // 아무것도 안입은 상태도 개수로 친다.
            closet.put(clothes[i][1], closet.getOrDefault(clothes[i][1], 1) + 1);
        }

        for (int i:closet.values())
            answer *= i;
        
        return answer-1;
    }
}
