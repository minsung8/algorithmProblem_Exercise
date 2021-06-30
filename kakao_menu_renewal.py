from itertools import combinations

def solution(orders, course):
    all_menu = ''
    for order in orders:
        all_menu += order
    all_menu = list(set(all_menu))
    
    answer = []
    temp_list = []

    for i in course:
        for order in orders:
            com = combinations(order, i)
            temp_list += com

    for temp in temp_list:
        temp_cnt = 0
        for order in orders:
            if len(set("".join(temp) + order)) == len(order):
                temp_cnt += 1

                if temp_cnt > 1:
                    answer.append([temp, temp_cnt])

    answer = sorted(answer, key=lambda x : (len(x[0]), -x[1]))

    result = []
    for i in range(len(answer)):
        
        if len(result) == 0:
            result.append(answer[i][0])
            temp = answer[i][1]
        
        elif len(answer[i][0]) == len(result[-1]) and temp == answer[i][1]:
            result.append(answer[i][0])
        
        elif len(result[-1]) < len(answer[i][0]):
            result.append(answer[i][0])
            temp = answer[i][1]

    result2 = []
    for answer in result:
        result2.append("".join(sorted(answer)))

    return sorted(set(result2))


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
