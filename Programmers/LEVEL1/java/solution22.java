package Programmers.LEVEL1.java;
import java.util.*;

public class solution22 {
    public int[] solution(long n) {
        int[] answer = {};
        String[] arr = Long.toString(n).split("");
        Collections.reverse(Arrays.asList(arr));
        
        answer = new int[arr.length];
        for (int i=0; i<arr.length; i++)
            answer[i] = Integer.parseInt(arr[i]);
        
        return answer;
    }
}
