// 프로그래머스 문제 : https://programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):

    answer_set_len = len(set(gems))  # 보석의 종류 개수
    temp_set = set()
    answer = []
    temp_dic = {}

    start = 0     # 시작 index
    end = 0       # 마지막 index

    if answer_set_len == 1:     # 보석의 종류가 한 종류일 경우
        return [1, 1]

    while end < len(gems) and start <= end:       # end index가 범위를 넘지 않고 start index가 end index보다 작을 경우

        if gems[end] not in temp_set:
            temp_set.add(gems[end])

        if gems[end] not in temp_dic.keys():
            temp_dic[gems[end]] = 1
        elif gems[end] in temp_dic.keys():
            temp_dic[gems[end]] += 1

        if len(temp_set) == answer_set_len:
            answer.append([start, end, end-start])
            if temp_dic[gems[start]] == 1:
                temp_set.remove(gems[start])
                del temp_dic[gems[start]]
            else:
                temp_dic[gems[start]] -= 1
            start += 1
            if temp_dic[gems[end]] == 1:
                del temp_dic[gems[end]]
                temp_set.remove(gems[end])
            else:
                temp_dic[gems[end]] -= 1

        else:
            end += 1

    answer = sorted(answer, key=lambda x: (x[2], x[0]))

    return [answer[0][0] + 1, answer[0][1] + 1]
