import java.lang.Math;

public class solution25 {
    public int solution(int n) {
        int answer = 1;
        if (n == 2)
            return answer;
        else if (n == 3)
            return answer;
        else{
            int nums[] = new int[n+1];
        
            int s = (int)Math.sqrt(n)+1;
            for (int i=2; i <= s; i++){
                if (nums[i] == 0){
                    for (int j=i+i; j <= n; j+=i){
                        nums[j] = 1;
                    }
                }
            }
            for (int i=2; i <= n; i++){
                if (nums[i] == 0)
                    answer++;
            }
        }
        
        return answer-1;
    }
}
