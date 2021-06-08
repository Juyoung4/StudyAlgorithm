public class solution35 {
    public int solution(int[] d, int budget) {
        int answer = 0;
        Arrays.sort(d);
        
        int total = 0;
        for(int i: d){
            if (total+i <= budget){
                total += i;
                answer++;
            }
            else{
                break;
            }
        }
        return answer;
    }
}
