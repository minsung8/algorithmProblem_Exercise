def solution(stock):        ## 한번의 거래로 가장 큰 이익 산출

    max_dic = {}
    
    for i in range(len(stock) - 1):
        max_dic[i] = max(stock[i+1:])
    max_dic[len(stock)-1] = 0
    answer_list = []

    for i in range(len(stock)):
        answer_list.append(max_dic[i] - stock[i])
        

    return max(answer_list)

print( solution([7, 1, 5, 3, 6, 4]) )
print( solution([3, 18, 7, 1, 5, 3 ,6 ,4]) )
