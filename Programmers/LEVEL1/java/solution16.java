import java.util.*;

public class solution16 {
    public boolean solution(String s) {
        if (s.length() == 4 || s.length() == 6){
            for (int i=0; i<s.length(); i++){
                if (!Character.isDigit(s.charAt(i))) // '0' <= s.charAt(i) && s.charAt(i) <= '9'라고 해도 됨
                    return false;
            }
            return true;
        }
        return false;
    }
}
