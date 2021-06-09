package Programmers.LEVEL1.java;

import java.util.*;

public class solution10 {
    public String solution(String[] seoul) {
        int idx = Arrays.asList(seoul).indexOf("Kim");
        return "김서방은 "+idx+"에 있다";
    }

    public static void main(String[] args) {
        solution10 result = new solution10();

        String[] s = {"jan","kim"};

        System.out.println(result.solution(s));
    }
}
