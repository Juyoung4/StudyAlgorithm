package Programmers.LEVEL1.java;
import java.util.*;

public class solution32 {
    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);
        Arrays.sort(completion);
        for (int i = 0; i < completion.length; i++){
            if (!(completion[i].equals(participant[i])))
                return participant[i];
        }
        return participant[participant.length-1];
    }
}
