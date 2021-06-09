package Programmers.LEVEL1.java;
import java.util.*;

public class solution33 {
    public int[] solution(int[] answers) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        int[] one = {1, 2, 3, 4, 5};
        int[] two = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] three = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int[] temp = new int[3];
        for (int i=0; i<answers.length; i++){
            if (one[i%5] == answers[i])
                temp[0]++;
            if (two[i%8] == answers[i])
                temp[1]++;
            if (three[i%10] == answers[i])
                temp[2]++;
        }
        
        answer.add(0);
        if (temp[1] > temp[answer.get(0)])
            answer.set(0, 1);
        else if (temp[1] == temp[answer.get(0)])
            answer.add(1);
        
        if (temp[2] > temp[answer.get(0)]){
            answer.clear();
            answer.add(2);
        }
        else if (temp[2] == temp[answer.get(0)])
            answer.add(2);
        
        int[] result = new int[answer.size()];
        for (int i=0; i <answer.size(); i++){
            result[i] = answer.get(i)+1;
        }
        return result;
    }
}
