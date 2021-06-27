from itertools import combinations

def solution(orders, course):
    answer = []
    all_menu = []
    for i in range(len(orders)):
        for j in range(len(orders[i])):
            if orders[i][j] not in all_menu:
                all_menu.append(orders[i][j])

    return all_menu

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
