package Programmers.LEVEL1.java;
import java.util.*;

public class solution31 {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        //초기화
        ArrayList<Integer> arr = new ArrayList<Integer>();
        for (int i=0; i<array.length; i++)
            arr.add(array[i]);
        
        ArrayList<Integer> sub = new ArrayList<Integer>(); //subList는 List형임
        for (int c=0; c<commands.length; c++){
            
            for (int i = commands[c][0]-1; i < commands[c][1]; i++)
                sub.add(arr.get(i)); //arrayList는 get으로 index 활용
            
            Collections.sort(sub);

            answer[c] = sub.get(commands[c][2]-1);
            
            sub.clear();
        }
        return answer;
    }

    public int[] solution2(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for(int i=0; i<commands.length; i++){
            int[] temp = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
            Arrays.sort(temp);
            answer[i] = temp[commands[i][2]-1];
        }

        return answer;
    }
}
