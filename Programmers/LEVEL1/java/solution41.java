public class solution41 {
    public String solution(String new_id) {
        String answer = "";
        //1 - 대문자 -> 소문자
        new_id = new_id.toLowerCase();
        //2 - 알파벳, 숫자, 빼기, 밑줄, 마침표 제외한 문자 모두 제거
        //3 - '.' 2번 이상이면 한번만 
        //4 - '.' 맨 앞과 맨 뒤에 있으면 제거(여기선 맨 앞만)
        char t;
        int len=0;
        for(int i=0; i<new_id.length(); i++){
            t = new_id.charAt(i);
            if (('a' <= t && t <= 'z') || t == '-' || t == '_' || t == '.' || ('0' <= t && t <= '9')){
                if (t=='.'){
                    if (len != 0 && answer.charAt(len-1) != '.'){
                        answer += t;
                        len++;
                    }
                }
                else{
                    answer += t;
                    len++;
                }
            }
        }
        
        //4 - '.' 맨 앞과 맨 뒤에 있으면 제거(여기선 맨 뒤만)
        if (len != 0 && answer.charAt(len-1) == '.'){
            answer = answer.substring(0,len-1); //substring소문자
            len--;
        }
        
        //5 - 빈 문자열이면 new_id = "a"
        if (len == 0){
            answer = "a";
            len = 1;
        }
        
        //7-new_id 2이하면 길이 3만들어서 제출
        char tt = answer.charAt(len-1);
        if (len == 1) answer = answer + tt + tt;
        if (len == 2) answer = answer + tt;
        
        //6 - 16자 이상이면 15자리까지 자르기
        if (len >= 16) {
            answer = answer.substring(0, 15);
            int temp = 0;
            if (answer.charAt(answer.length()-1) == '.'){
                for (int i=14; i>0; i--){
                    if (answer.charAt(i) != '.'){
                        temp = i;
                        break;
                    }
                }
                answer = answer.substring(0, temp+1);
            }
        }
        System.out.println(answer + ' ' + answer.length()+ ' ' + len);
        return answer;
    }
}
