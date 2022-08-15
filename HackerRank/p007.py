# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true

def simpleArraySum(ranked, player):
    # Write your code here
    

    all_list = sorted(list(set(ranked + player)), reverse=True)

    ranked_dic = {}

    for i in range(len(ranked)):
        ranked_dic[ranked[i]] = True

    temp_rank = 1
    for i in range(len(all_list)):
        if ranked_dic.get(all_list[i]):
            ranked_dic[all_list[i]] = temp_rank
            temp_rank += 1
        else:
            ranked_dic[all_list[i]] = temp_rank
    
    answer = []
    for i in range(len(player)):
        answer.append( ranked_dic[player[i]] )
    
    return answer

#print(simpleArraySum([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))     # 6 4 2 1
print(simpleArraySum([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102] ))    # 6 5 4 2 1


# 102 100 90 80 77 75 65 60 50
#      1   2  3     4     5
