# 모의 고사
# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
# 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.
#
# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
#
# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.
#
# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
# 입출력 예
# answers	    return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]

def solution(answers):
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    person1_count = 0
    person2_count = 0
    person3_count = 0

    for i in range(0, len(answers)):
        if person1[i % len(person1)] == answers[i]:
            person1_count += 1
        if person2[i % len(person2)] == answers[i]:
            person2_count += 1
        if person3[i % len(person3)] == answers[i]:
            person3_count += 1

    max_count = max(person1_count, person2_count, person3_count)

    if person1_count == person2_count == person3_count:
        return [1, 2, 3]
    elif person1_count == person2_count and max_count == person1_count:
        return [1, 2]
    elif person1_count == person3_count and max_count == person1_count:
        return [1, 3]
    elif person2_count == person3_count and max_count == person2_count:
        return [2, 3]

    if person1_count == max_count:
        return [1]
    elif person2_count == max_count:
        return [2]
    else:
        return [3]


answer_list = [1, 3, 2, 4, 2]
print(solution(answer_list))


def programmers(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx % len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx % len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx + 1)

    return result


print(programmers(answer_list))
