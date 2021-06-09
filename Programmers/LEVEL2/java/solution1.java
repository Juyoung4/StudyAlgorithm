package Programmers.LEVEL2.java;
import java.util.*;

public class solution1 {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        //1. 사전순 + 길이순으로 sort한다.
        Arrays.sort(phone_book);
        for (int i=1; i < phone_book.length; i++){
            if (phone_book[i].startsWith(phone_book[i-1])){
                answer = false;
                break;
            }
        }
        return answer;
    }
}
