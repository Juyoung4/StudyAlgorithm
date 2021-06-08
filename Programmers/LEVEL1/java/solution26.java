public class solution26 {
    public int gcd(int a, int b){
        int temp = 0;
        while (b != 0){
            temp = a%b;
            a = b;
            b = temp;
        }

        return a;
    }    
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        answer[0] = gcd(m, n);
        answer[1] = (n*m) / answer[0];
        
        return answer;
    }
}
/*

최대 공약수 : gcd => %를 이용해 구할 수 있음
최대 공배수 : 두 자연수의 곱 / 최대공약수
*/