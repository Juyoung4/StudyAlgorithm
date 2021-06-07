public class solution24 {
    public long solution(long n) {
        if (n == (long)Math.pow((long)Math.sqrt(n), 2))
            //type 조심하기
            return (long)Math.pow((long)Math.sqrt(n)+1, 2);
        else
            return -1;
    }
}
