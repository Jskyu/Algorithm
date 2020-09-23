package level1.최대공약수와_최소공배수;

class Solution {
    public int[] solution(int n, int m){

        int big = Math.max(n, m);
        int small = Math.min(n, m);
        int gcd;
        int lgc;

        while(true){
            int nmg = big % small;
            if(nmg == 0){
                gcd = small;
                lgc = (n*m)/small;
                break;
            }

            big = small;
            small = nmg;
        }
        int[] answer = {gcd, lgc};

        return answer;
    }
}