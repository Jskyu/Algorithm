/*
모의고사
문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
입출력 예
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
 */

function solution(answers) {
    let answer = [];
    let num = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]];
    let answerList = [0, 0, 0];
    for (let i = 0; i < answers.length; i++) {
        for (let j = 0; j < num.length; j++) {
            if (num[j][i% (num[j].length)] === answers[i]) {
                answerList[j]++;
            }
        }
    }

    let max_count = Math.max(answerList[0], answerList[1], answerList[2])
    for(let i = 0; i < answerList.length; i++) {
        if(max_count === answerList[i])
            answer.push(i + 1);
    }

    return answer;
}

let answerArr = [1, 3, 2, 4, 2, 1, 3, 2, 4, 2, 1, 3, 2, 4, 2, 1, 3, 2, 4, 2];
console.log(solution(answerArr));
console.log(solution2(answerArr));

function solution2(answers){
    const A = '12345'.split('')
    const B = '21232425'.split('')
    const C = '3311224455'.split('')

    return [A,B,C].map((p, i) => ({
        i: i+1, s: (answers .map((v, i) => v === Number(p[i % p.length])) .filter(c => c).length)
    }))
        .sort((a,b) => b.s - a.s)
        .filter((v,i,a) => a[0].s === v.s)
        .map(v => v.i)
        .sort((a,b) => a - b);
}