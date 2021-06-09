package Programmers.LEVEL1.java;
import java.util.*;
public class solution27 {
    public int solution(long num) { //long으로 타입 변경 -> 오버플로우 발생
        int answer = -1;
        for (int i=0; i < 500; i++){
            if (num == 1){
                answer = i;
                break;
            }
            if (num%2 == 0){
                num /= 2;
            }
            else{
                num = num*3+1; 
            }
        }
        return answer;
    }
}
