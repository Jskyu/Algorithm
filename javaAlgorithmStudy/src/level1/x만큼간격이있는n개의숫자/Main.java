package level1.x만큼간격이있는n개의숫자;

public class Main {
    public static void main(String[] args){

        Solution solution = new Solution();

        int x = 4;
        int n = 3;

        for(long l : solution.solution(x, n)){
            System.out.print(l + "  ");
        }
    }
}
