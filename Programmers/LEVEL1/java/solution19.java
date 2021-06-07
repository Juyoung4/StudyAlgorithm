public class solution19 {
    public String solution(String phone_number) {
        String answer = "";
        int bound = phone_number.length()-4;
        answer = "*".repeat(bound) + phone_number.substring(bound);
        return answer;
    }
    public String solution2(String phone_number) {
        char[] ch = phone_number.toCharArray(); //String to Char
        for(int i = 0; i < ch.length - 4; i ++){
            ch[i] = '*';
        }
        return String.valueOf(ch);
    }
    public String solution3(String phone_number) {
        return phone_number.replaceAll(".(?=.{4})", "*"); // 정규식
        // 첫번째 . => 임의의 문자 하나 의미 / (?=.{숫자}) => 뒷쪽에 임의의 문자 한개를 제외하고 선택(즉 숫자만큼 제외하고 선택)
    }
}
