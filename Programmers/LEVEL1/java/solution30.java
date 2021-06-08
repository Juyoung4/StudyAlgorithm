public class solution30 {
    public String solution(String s, int n) {
        String answer = "";
        char c_temp;
        int temp = 0;
        for (int i=0; i<s.length(); i++) {
            c_temp = s.charAt(i);
            if (c_temp == ' '){
                answer += " ";
                continue;
            }
            
            temp = (int)c_temp; // 'A'-65 ~ Z-90 / 'a-97 ~ 'z'-122
            if ((65 <= temp) && (temp <= 90)){
                temp = temp+n;
                if (temp > 90)
                    temp = 65 + (temp-91);
            }
            else{
                temp = temp+n;
                if (temp > 122)
                    temp = 97 + (temp-123);
            }
            System.out.println(temp);
            answer += (char)temp;            
        }
        return answer;
    }
}
