package level1;

import java.util.Arrays;
import java.util.Collections;

public class solution2 {
    public String solution(String s) {
        String answer = "";
        String[] sArray = s.split("");
        Arrays.sort(sArray);

        Collections.reverse(Arrays.asList(sArray));

        answer = String.join("", sArray);

        return answer;
    }

    public String solution2(String s) {
        char[] array = s.toCharArray(); // string to char array
        Arrays.sort(array); // array sort
        // array를 다시 string으로 변환 
        // stringBuilder를 이용하여 string reverse()
        return new StringBuilder(new String(array)).reverse().toString(); // @3
    }

    //TestCase
    public static void main(String[] args) {
        solution2 descendingString = new solution2();

        String s = "Zbcdefg";

        System.out.println(descendingString.solution(s));
    }
}
