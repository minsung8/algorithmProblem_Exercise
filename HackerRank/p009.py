# https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true

def solution(k, s):

    dic = {}
    answer = 0
    for i in s:
        temp = i % k
        if temp in dic: dic[temp] += 1
        else: dic[temp] = 1

    for i in range(((k + 1) // 2), k):
        temp = k - i

        if i == temp and i in dic:
            answer += 1
            continue

        if i in dic and temp in dic:
            answer += max(dic[i], dic[temp])
        elif i in dic:
            answer += dic[i]
        elif j in dic:
            answer += dic[j]

    return answer

print(solution(3, [1, 7, 2, 4]))    # 3
print(solution(7, [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]))

# 2 6 3 2 2
# 6 3 2 