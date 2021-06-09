package Programmers.LEVEL1.java;
import java.util.*;
import java.util.Scanner;

public class solution20 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(); //가로
        int b = sc.nextInt(); //세로
        
        for (int i=1; i<=b; i++){
            System.out.println("*".repeat(a));
        }
    }
}
