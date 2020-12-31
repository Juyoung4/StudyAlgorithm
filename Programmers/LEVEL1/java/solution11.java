package level1;

public class solution11 {
    public String solution(String s) {
        int mid = s.length()/2;
        return s.length()%2 == 0? s.substring(mid-1,mid+1) : s.substring(mid,mid+1);
    }
    
    public static void main(String[] args) {
        solution11 result = new solution11();

        String s = "abced";

        System.out.println(result.solution(s));
    }
}
