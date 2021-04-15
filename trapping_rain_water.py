def solution(block):

    answer = 0
    start = 0
    end = 0

    while end < len(block):
        end += 1
        if end == len(block):
            break

        if block[start] <= block[end]:
            start = end
        
        elif block[start] > block[end] and block[start] <= max(block[start+1:]):
            answer += block[start] - block[end]
        
        else:
            start += 1
            
    return answer

print( solution([0,1,0,3,1,0,1,3,2,3,3,1]) )