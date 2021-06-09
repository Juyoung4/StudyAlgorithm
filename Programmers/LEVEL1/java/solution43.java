package Programmers.LEVEL1.java;
import java.util.*;

public class solution43 {
    public int solution(int[] nums) {
        int answer = 0;
        int N = nums.length/2;
        Integer array[] = Arrays.stream(nums).boxed().toArray(Integer[]::new);
        Set<Integer> hashSet = new HashSet<>(Arrays.asList(array));
        
        if (N >= hashSet.size()) answer = hashSet.size();
        else answer = N;

        return answer;
    }
}
