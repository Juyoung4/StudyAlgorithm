package Programmers.LEVEL1.java;
import java.util.*;

public class solution18 {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        
        long temp = 0;
        for (int i=0; i < n; i++){
            temp += x;
            answer[i] = temp;
        }
        return answer;
    }
}
