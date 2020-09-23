package level1.문자열내림차순정렬;

import java.util.Arrays;

public class Main {
    public static void main(String[] args){
        String s = "Zbcdefg";

        System.out.println("solution(s) = " + solution(s));
    }

    private static String solution(String s){
        String answer = "";
        char[] chars = s.toCharArray();
        Arrays.sort(chars);

        answer = new StringBuilder(new String(chars)).reverse().toString();

        return answer;
    }


}
