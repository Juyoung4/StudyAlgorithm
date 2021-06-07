//문자열 내 p와 y의 개수
public class solution14 {
    boolean solution(String s) {
        
        s = s.toLowerCase();
        int p_count = 0;
        int y_count = 0;
        for (int i=0; i < s.length(); i++){
            if (s.charAt(i) == 'p'){
                p_count++;
            }
            else if (s.charAt(i) == 'y'){
                y_count++;
            }
            
        }
        
        if (p_count == y_count) {
            return true;
        }
        else{
            return false;
        }
    }
}
