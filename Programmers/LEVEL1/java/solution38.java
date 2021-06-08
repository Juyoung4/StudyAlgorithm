import java.util.*;
import java.lang.Math;

public class solution38 {
    public int solution(String dartResult) {
        int answer = 0;
            
        Stack<Integer> stack = new Stack<Integer>();
        int temp_score = -1;
        char temp;
        int t1 = 0;
        int t2 = 0;
        for (int i=0; i < dartResult.length(); i++){
            temp = dartResult.charAt(i);
            if ('0' <= temp && temp <= '9'){
                if (temp_score == -1)
                    temp_score = temp - '0'; //또는 valueOf
                else
                    temp_score = 10;
            }
            else if (temp == 'S' || temp == 'D' || temp == 'T'){
                if (temp == 'D') temp_score = (int)Math.pow((double)temp_score, 2); // math 안쓰고 temp_score = temp_score*temp_Score하는게 나을지도..
                else if (temp == 'T') temp_score = (int)Math.pow((double)temp_score, 3);
                stack.push(temp_score);
                temp_score = -1;
            }
            else {
                if (temp == '*'){
                    if (i <= 2){
                        stack.push(stack.pop()*2);
                    }
                    else{
                        t1 = stack.pop()*2;
                        t2 = stack.pop()*2;
                        stack.push(t2);
                        stack.push(t1);
                    }
                }
                else { // '#이면'
                    stack.push(stack.pop()*(-1));          
                }
            }
        }
        for (int s : stack)
            answer += s;
        return answer;
    }
}
