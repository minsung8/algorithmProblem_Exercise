def solution(s, t):
    sorted_s = sorted(s)
    sorted_t = sorted(t)

    if sorted_s == sorted_t:
        return True
    
    return False  



print(solution('anagram', 'nagaram'))
print(solution('rat', 'car'))
