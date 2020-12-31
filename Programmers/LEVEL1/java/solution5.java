package level1;

public class solution5 {
    public String solution(int num) {
        return num%2 == 0? "Even" : "Odd";
    }

    public static void main(String[] args) {
        solution5 result = new solution5();

        int n = 0;

        System.out.println(result.solution(n));
    }

}
