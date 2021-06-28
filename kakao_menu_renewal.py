from itertools import combinations

def solution(orders, course):

    answer_dic = {}

    for i in course:
        temp_list = []
        for order in orders:
            temp = list(combinations(order, i))
            temp_list.append(temp)
        
        for j in range(len(temp_list) - 1):
            for k in range(len(temp_list[j])):

                for l in range(j, len(temp_list)):
                    if temp_list[j][k] in temp_list[l]:

                        if temp_list[j][k] in answer_dic:
                            answer_dic[temp_list[j][k]] += 1
                        else:
                            answer_dic[temp_list[j][k]] = 1

    return answer_dic 

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
#print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
#print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
