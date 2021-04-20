def solution(stock):        ## 한번의 거래로 가장 큰 이익 산출

    _min = 99999
    temp_answer = 0

    for i in range(len(stock)):
        if stock[i] < _min:
            _min = stock[i]
        
        if temp_answer < stock[i] - _min:
            temp_answer = stock[i] - _min

    return temp_answer

print( solution([7, 1, 5, 3, 6, 4]) )
print( solution([3, 18, 7, 1, 5, 3 ,6 ,4]) )