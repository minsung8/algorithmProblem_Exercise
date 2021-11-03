def solution(s):

    for temp_s in s:
        temp_idx = temp_s.index('110')

        for i in range(len(temp_s)-3):
            if temp_s[i:i+3] == '111' and i < temp_idx:
                pass

        

    return 

print(solution(["1110","100111100","0111111010"]))
# ["1101","100110110","0110110111"]
