# https://www.hackerrank.com/challenges/lilys-homework/problem?isFullScreen=true


def lilysHomework(arr):
    # Write your code here

    return min(work(arr, True), work(arr, False))


def work(arr, flag):

    dic = {}
    idx_dic = {}
    answer = 0

    for i in range(len(arr)):
        dic[arr[i]] = i
        idx_dic[i] = arr[i]

    if flag: front_arr = sorted(arr)
    else: front_arr = sorted(arr, reverse=True)

    for i in range(len(front_arr)):

        if front_arr[i] != idx_dic[i]:
            
            temp_idx = dic[front_arr[i]]

            dic[front_arr[i]] = i
            dic[idx_dic[i]] = temp_idx 

            idx_dic[temp_idx] = idx_dic[i]
            idx_dic[i] = front_arr[i]
            answer += 1

    return answer


print(lilysHomework([2, 5, 3, 1]))  # 2
print(lilysHomework([3, 4, 2, 5, 1]))   # 2


# 1 5 3 2 

# temp_idx = 3 
# dic[3] = 