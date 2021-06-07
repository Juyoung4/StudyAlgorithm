//같은 숫자는 싫어
public class solution12 {
    public int[] solution(int []arr) {
        int[] answer = {};
        int len = arr.length;

        ArrayList<Integer> result = new ArrayList<Integer>();

        int pre = arr[0];
        result.add(pre);


        for (int i=1; i < len; i++){
            if (pre != arr[i]){
                pre = arr[i];
                result.add(pre);
            }                
        }

        int n = result.size();
        answer = new int[n];
        for (int i=0; i < n; i++){
            answer[i] = result.get(i);
        }

        return answer;
    }

    // 다른 사람 풀이 -> for each문을 쓰면 더 간편!
    public int[] solution2(int []arr) {
        ArrayList<Integer> tempList = new ArrayList<Integer>();
        int preNum = 10;
        for(int num : arr) {
            if(preNum != num)
                tempList.add(num);
            preNum = num;
        }       
        int[] answer = new int[tempList.size()];
        for(int i=0; i<answer.length; i++) {
            answer[i] = tempList.get(i).intValue();
        }
        return answer;
    }
}


