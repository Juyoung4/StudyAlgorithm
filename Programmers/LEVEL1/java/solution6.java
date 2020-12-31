package level1;

public class solution6 {
    public String solution(int n) {
        String answer = "";
        for(int i = 1; i<=n; i++){
            if(i%2 != 0){
                answer += "수";
            }
            else{
                answer += "박";
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        solution6 result = new solution6();

        int n = 3;

        System.out.println(result.solution(n));
    }
}
