def solution(childs, cookies):

    childs = sorted(childs)
    cookies = sorted(cookies)

    answer = 0
    child_i = 0
    cookie_i = 0

    while cookie_i < len(cookies) and child_i < len(childs):
        
        if childs[child_i] <= cookies[cookie_i]:
            answer += 1
            child_i += 1
            cookie_i += 1
        else:
            cookie_i += 1

    return answer


print(solution([1,2,3], [1,1]))
print(solution([1,2], [1,2,3]))