package Programmers.LEVEL1.java;
import java.util.*;

public class solution34 {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        int[] checks = new int[n];
        
        for (int l : lost)
            checks[l-1]--;
        for (int r : reserve)
            checks[r-1]++;
        
        for (int i=0; i<n; i++){
            if (i==0){
                if ((checks[i]==1) && (checks[i+1]==-1)){
                    checks[i]--;
                    checks[i+1]++;
                }
            }
            else if (i== n-1){
                if ((checks[i]==1) && (checks[i-1]==-1)){
                    checks[i]--;
                    checks[i-1]++;
                }
            }
            else {
                if ((checks[i]==1) && (checks[i-1]==-1)){
                    checks[i]--;
                    checks[i-1]++;
                }
                else if ((checks[i]==1) && (checks[i+1]==-1)){
                    checks[i]--;
                    checks[i+1]++;
                }
            }
        }
        
        for (int c: checks){
            if (c >= 0)
                answer++;
        }
        return answer;
    }
}
