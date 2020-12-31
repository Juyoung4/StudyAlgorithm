package level1;

public class solution4 {
    public int solution(int n) {
        int answer = 0;
        if (n <= 0){
            return -1;
        }
        for(int i=1; i<=n; i++){
            if (n%i == 0){
                answer += i;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        solution4 result = new solution4();

        int n = 0;

        System.out.println(result.solution(n));
    }

}
