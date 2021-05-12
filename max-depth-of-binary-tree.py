def solution(tree):
    
    answer = 0
    temp = 1
    length_tree = len(tree)
    while length_tree > 0:
        
        length_tree -= temp
        temp *= 2
        answer += 1

    return answer

print(solution([3, 9, 20, 0, 0, 15, 7]))