package level1;

import java.util.*;

public class solution8 {
    public int[] solution(int[] arr, int divisor) {
        List<Integer> temp = new ArrayList<>();
        for(int i = 0; i < arr.length; i++){
            if (arr[i] % divisor == 0){
                temp.add(arr[i]);
            }
        }
        if (temp.isEmpty()) {
            temp.add(-1);
        }
        int[] answer = new int[temp.size()];
        for(int i = 0; i < answer.length; i++){
            answer[i] = temp.get(i);
        }
        Arrays.sort(answer);
        return answer;
    }
    public static void main(String[] args) {
        solution8 result = new solution8();

        int[] arr = {5, 9, 7, 10};

        int divisor = 3;

        System.out.println(result.solution(arr, divisor));
    }
}
