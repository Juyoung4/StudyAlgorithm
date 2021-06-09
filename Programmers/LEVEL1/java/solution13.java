// 문자열 내 마음대로 정렬하기
package Programmers.LEVEL1.java;
import java.util.*;

public class solution13 {
    public String[] solution(String[] strings, int n) {
        Arrays.sort(strings, new Comparator<String>() {
            public int compare(String s1, String s2) {
                if (s1.charAt(n) > s2.charAt(n)) {
                    return 1;
                } else if (s1.charAt(n) < s2.charAt(n)) {
                    return -1;
                } else {
                    return s1.compareTo(s2);
                }
            }
        });

        return strings;
    }
}
