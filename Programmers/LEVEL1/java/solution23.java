package Programmers.LEVEL1.java;
import java.util.*;

public class solution23 {
    public boolean solution(int x) {
        int sum = 0;
        int temp = x;
        while (temp > 0){
            sum += (temp % 10);
            temp /= 10;
        }
        if (x % sum == 0)
            return true;
        else
            return false;
    }
}
