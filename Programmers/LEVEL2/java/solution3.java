package Programmers.LEVEL2.java;
import java.util.*;

public class solution3 {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = {};
        ArrayList<Integer> arr = new ArrayList<Integer>();
        Queue<Integer> queue = new LinkedList<Integer>();

        int days = 0;
        
        for (int i=0; i<progresses.length; i++){
            //1. 계산
            days = (100 - progresses[i]);
            if (days%speeds[i] != 0) days = days/speeds[i] + 1;
            else days = days/speeds[i];
            
            if (!queue.isEmpty() && queue.peek() < days) {
                arr.add(queue.size());
                queue.clear();
            }
            queue.offer(days);
        }
        arr.add(queue.size());
        
        answer = new int[arr.size()];
        for (int i=0; i < arr.size(); i++) {
            answer[i] = arr.get(i);
        }
        return answer;
    }
}
