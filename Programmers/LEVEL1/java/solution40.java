package Programmers.LEVEL1.java;
import java.util.*;

public class solution40 {
    public static void main(String[] args) {
        solution40 two = new solution40();
        
        int[] t = {1};
        int[] result = two.solution(3, t);
        for (int r : result)
            System.out.println(r);
    }

    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        int[] temp = new int[N];
        int total = 0;
        for (int i=0; i<stages.length; i++){
            if (stages[i]==N+1) total++;
            else temp[stages[i]-1]++;
        }

        // 구조체 선언
        node[] scores = new node[N];
        
        //실패율
        for (int i=N-1; i>=0; i--){
            total += temp[i];
            if ((temp[i] != 0) && (total != 0)) scores[i] = new node(i+1, (double)temp[i]/total);
            else scores[i] = new node(i+1, 0);
        }
        
        // sort 함수 생성 -> [1] 점수 기준(내림) [2] 인덱스 기준(오름)
        Comparator<node> failsort = new Comparator<node>(){
            @Override
            public int compare(node o1, node o2) {
                if (o1.score == o2.score) return Integer.compare(o1.idx, o2.idx); //양수 오름 차순?
                return -Double.compare(o1.score, o2.score); //음수 내림 차순
            }
        };
        //sort하기
        Arrays.sort(scores, failsort);
        for (int i=0; i<N; i++)
            answer[i] = scores[i].idx;
        return answer;
    }
    
    //node라는 class 지정 -> 구조체
    class node{
        int idx;
        double score;
        
        public node(int idx, double score){
            this.idx = idx;
            this.score = score;
        }
    }
}
