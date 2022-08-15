# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true

def simpleArraySum(ranked, player):
    # Write your code here

    ranked_set_list = sorted(list(set(ranked)), reverse=True)
    all_list = sorted(list(set(ranked + player)), reverse=True)
    answer_list = []
    for i in range(len(all_list)):
        if all_list[i] in ranked_set_list:
            answer_list.append([all_list[i], ranked_set_list.index(all_list[i]) + 1])
        else:
            answer_list.append([all_list[i], -1])

    rank_dic = {}
    for i in range(len(answer_list) - 1):
        if answer_list[i][1] == -1:
            rank_dic[answer_list[i][0]] = answer_list[i + 1][1]
        else:
            rank_dic[answer_list[i][0]] = answer_list[i][1]
    if answer_list[-1][1] == -1:
        rank_dic[answer_list[-1][0]] = len(ranked_set_list) + 1
    else:
        rank_dic[answer_list[-1][0]] = answer_list[-1][1]

    answer = []
    for p in player:
        answer.append(rank_dic[p])
    return answer

    
print(simpleArraySum([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))     # 6 4 2 1

# 120 100 50 40 25 20 10 5
#      1   2  3     4  5 
