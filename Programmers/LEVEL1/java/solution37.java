public class solution37 {
    public String solution(int[] numbers, String hand) {
        StringBuilder bd = new StringBuilder();
        int left = 10;
        int right = 11;
        int keypad[][] = {{3,1}, {0,0}, {0,1},{0,2}, {1,0}, {1,1},{1,2},{2,0}, {2,1}, {2,2}, {3,0}, {3,2}};
        for(int num : numbers){
            if (num == 1 || num == 4 || num == 7){
                bd.append("L");
                left = num;
            }
            else if (num == 3 || num == 6 || num ==9){
                bd.append("R");
                right = num;
            }
            else{
                int temp1 = Math.abs(keypad[left][0] - keypad[num][0]) + Math.abs(keypad[left][1] - keypad[num][1]);
                int temp2 = Math.abs(keypad[right][0] - keypad[num][0]) + Math.abs(keypad[right][1] - keypad[num][1]);
                if (temp1 < temp2){
                    bd.append("L");
                    left = num;
                }
                else if(temp1 > temp2){
                    bd.append("R");
                    right = num;
                }
                else{
                    if (hand.equals("right")) {
                        bd.append("R");
                        right = num;
                    }
                    else{
                        bd.append("L");
                        left = num;
                    }
                }
            }
            
        }
        return bd.toString();
    }
}
