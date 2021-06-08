public String[] solution(int n, int[] arr1, int[] arr2) {
    String[] answer = new String[n];
    String temp;
    int check = 0;
    for (int i=0; i<n; i++){
        //binary로 변환하는 법 Integer.toBinaryString(a)
        temp = Integer.toBinaryString(arr1[i] | arr2[i]);
        answer[i] = "";
        check = n-temp.length();
        if (check != 0)
            answer[i] = " ".repeat(check);
        for (int j=0; j<temp.length(); j++)
            if (temp.charAt(j)=='0')
                answer[i] += " ";
            else
                answer[i] +="#";
    }
    return answer;
}