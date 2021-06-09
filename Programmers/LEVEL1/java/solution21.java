package Programmers.LEVEL1.java;
import java.util.*;

public class solution21 {
    public long solution(long n) {
        //문자열은 sort가 없음!
        
        char[] temp = Long.toString(n).toCharArray();
        Arrays.sort(temp);
        
        String answer = "";
        for (int i=temp.length-1; i >= 0; i--){
            answer += temp[i];
        }
      
        return Long.parseLong(answer);
    }
}
