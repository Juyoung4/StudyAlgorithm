package Programmers.LEVEL2.java;

public class solution5 {
    public static void main(String[] args) {
        solution5 descendingString = new solution5();

        int[] temp = {1, 1, 1, 1, 1};

        System.out.println(descendingString.solution(temp, 3));
    }

    public int solution(int[] numbers, int target) {
        int answer = 0;
        answer = dfs(numbers, 0, 0, target);
        return answer;
    }
    
    public int dfs(int[] nums, int idx, int result, int target){
        if (idx == nums.length){
            System.out.println(result);
            if (result == target) return 1;
            else return 0;
        }
        return dfs(nums, idx+1, result+nums[idx], target) + dfs(nums, idx+1, result-nums[idx], target);
    }
}
