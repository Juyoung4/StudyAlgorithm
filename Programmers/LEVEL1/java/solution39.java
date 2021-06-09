package Programmers.LEVEL1.java;
import java.util.*;

public class solution39 {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> stack = new Stack<Integer>();
        int len = board.length;
        
        for (int m:moves){
            //먼저 인형 집기
            for (int i = 0; i < len; i++) //행 움직임
                if (board[i][m-1] != 0) {
                    if ((stack.empty()==false) && (board[i][m-1] == stack.peek())){
                        stack.pop();
                        answer += 2;
                    }
                    else{
                        stack.push(board[i][m-1]);
                    }
                    board[i][m-1] = 0;
                    break;
                }
            //인형 집었음 stack 터졌는지 확인
        }

        return answer;
    }
}
