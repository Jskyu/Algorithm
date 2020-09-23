package level1.하샤드_수;

class Solution {
    public boolean solution(int x) {
        int i = 0;
        String[] split = String.valueOf(x).split("");
        for(String s : split){
            i += Integer.parseInt(s);
        }
        return x % i == 0;
    }
}