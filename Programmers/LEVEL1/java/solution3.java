package Programmers.LEVEL1.java;

import java.util.Arrays;

public class solution3 {
    public double solution(int[] arr) {
        int total = 0;
        for(int i=0;i<arr.length;i++){
            total += arr[i];
        }
        return (double)total/arr.length;
    }

    public double solution2(int[] arr) {
        return (int) Arrays.stream(arr).average().orElse(0);
    }

    public static void main(String[] args) {
        solution3 result = new solution3();

        int[] arr = {1,2,3,4};

        System.out.println(result.solution(arr));
    }
}
