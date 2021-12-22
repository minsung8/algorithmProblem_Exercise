def solution(a, b, g, s, w, t):
    answer = 0

    for i in range(len(g)):
        temp_w = w[i]
        temp_t = t[i]
        temp_g = g[i]
        temp_s = s[i]
        while True:
            
            now = [0, 0]        # 수레 (금, 은) 
            print(a, b)
            answer += temp_t
            if a >= temp_w:     # 금 담기 
                a -= temp_w
                now[0] += temp_w
            else:
                now[0] += a
                a = 0
            
            if now[0] < temp_w:
                temp_w_2 = temp_w - now[0]
                if b >= temp_w_2:     # 은 담기 
                    b -= temp_w
                    now[1] += temp_w_2
                else:
                    now[1] += b
                    b = 0
            
            if a == 0 and b == 0:
                break

            temp_g -= now[0]    # 채우기 
            temp_s -= now[1]
            answer += temp_t
        print(answer)
    return answer

#print(solution(10, 10, [100], [100], [7], [10]))        #10
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))        #10
