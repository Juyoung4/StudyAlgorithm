package Programmers.LEVEL2.java;
import java.util.*;

public class solution4 {
    public static void main(String[] args) {
        solution4 descendingString = new solution4();

        int[] temp = {7, 4, 5, 6};

        System.out.println(descendingString.solution(2, 10, temp));
    }

    public int solution(int bridge_length, int weight, int[] truck_weights) {
        
        int cur_weight = 0;
        Queue<Integer> stack = new LinkedList<Integer>();
        Queue<Integer> stack2 = new LinkedList<Integer>();

        int answer = 1;
        int idx = 1;
        stack.offer(answer);
        stack2.offer(answer-1);
        cur_weight = truck_weights[idx-1];
        answer++;
        
        while (!stack.isEmpty()) {
            //1. 다리 다 건넌 트럭 빼기
            System.out.println("check1 : "+stack+" "+stack2+ " "+idx+" "+answer+" "+cur_weight);
            while (!stack.isEmpty() && (stack.peek()+bridge_length == answer)){
                cur_weight -= truck_weights[stack2.poll()];
                stack.poll();
            }              
            
            //2. 다리 건너는 트럭 추가
            if ((idx < truck_weights.length) && (cur_weight+truck_weights[idx] <= weight)) {
                cur_weight += truck_weights[idx];
                stack.offer(answer);
                stack2.offer(idx);
                idx++;
            }
            System.out.println("check1 : "+stack+" "+stack2+ " "+idx+" "+answer+" "+cur_weight);
            answer++;
        }
        System.out.println("check3 : "+stack);
        return answer-1;
    }
}
