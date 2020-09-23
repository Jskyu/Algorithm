package level1.완주하지못한선수;

public class Main {

    public static void main(String[] args){
        Solution solution = new Solution();

        String[] participant = {"marina", "josipa", "nikola", "vinko", "filipa"};
        String[] completion = {"josipa", "filipa", "marina", "nikola"};

        System.out.println(solution.solution(participant, completion));
    }
}
