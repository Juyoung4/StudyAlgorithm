package level1;

import java.util.*;

public class solution7 {
    public int solution(int n) {
        int answer = 0;

        while (n >= 1){
            answer += n%10;
            n /= 10;
        }

        return answer;
    }
    public static void main(String[] args) {
        solution7 result = new solution7();

        int n = 3;

        System.out.println(result.solution(n));
    }
}
