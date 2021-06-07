import java.util.*;

public class solution17 {
    public String solution(String s) {
        String answer = "";
        int cnt = 0;
        for (int i=0; i < s.length(); i++){
            char temp = s.charAt(i);
            if (temp == ' '){//공백이면
                cnt = 0;
                answer += ' ';
            }
            else{
                if (cnt%2 == 0){//단어 짝수-대문자
                    answer += String.valueOf(temp).toUpperCase();//char형-> string으로
                }
                else{
                    answer += String.valueOf(temp).toLowerCase();
                }
                cnt++;
            }
        }
        return answer;
    }
}
