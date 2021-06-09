package Programmers.LEVEL1.java;

import java.util.*;

public class solution9 {
    public int[] solution(int[] arr) {
        if(arr.length == 1){
            return new int[]{-1};
        }
        int min = Arrays.stream(arr).min().getAsInt();
        return Arrays.stream(arr).filter(x -> x != min).toArray();
    }

    public static void main(String[] args) {
        solution9 result = new solution9();

        int[] arr = {5, 9, 7, 10};

        System.out.println(result.solution(arr));
    }
}
