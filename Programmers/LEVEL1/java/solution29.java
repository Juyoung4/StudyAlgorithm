public class solution29 {
    public static void main(String[] args) {
        solution29 two = new solution29();

        System.out.println(two.solution(1, 2));
    }

    public String solution(int a, int b) {
        String[] answer = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
        
        int jumps = 0;
        for (int i = 1; i <= 12; i++){
            if (i == a){
                jumps += b;
                break;
            }
            if (i == 2)
                jumps += 29;
            else if ((i == 4) || (i == 6) || (i == 9) || (i == 11))
                jumps += 30;
            else
                jumps += 31;
        }

        return answer[(5+(jumps-1)%7)%7];
    }

}
