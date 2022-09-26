# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?isFullScreen=true


def activityNotifications(expenditure, d):
    # Write your code here

    def get_median(temp_list, d):
        temp_cnt = 0
        
        if d % 2 == 0:
            mid1, mid2 = 0, 0
            for j in range(len(temp_list)):

                if temp_list[j] > 0:
                    temp_cnt += temp_list[j]
                
                if mid1 == 0 and temp_cnt >= d // 2:
                    mid1 = j
                if mid2 == 0 and temp_cnt >= d // 2 + 1:
                    mid2 = j
                    return (mid1 + mid2) / 2

        else:
            for j in range(len(temp_list)):
                if temp_list[j] > 0:
                    temp_cnt += temp_list[j]
                
                if temp_cnt >= d // 2 + 1:
                    return j

    answer = 0
    temp_list = [0] * 200

    for i in range(d):
        temp_list[expenditure[i]] += 1

    for i in range(d, len(expenditure)):
        if i < d:
            temp_list[expenditure[i]] += 1
            continue

        median = get_median(temp_list, d)

        if expenditure[i] >= 2 * median:
            answer += 1

        temp_list[expenditure[i - d]] -= 1
        temp_list[expenditure[i]] += 1

    return answer

print(activityNotifications([1, 2, 3, 4, 4], 4))    # 0
print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))    # 2
print(activityNotifications([10, 20, 30, 40, 50], 3))   # 1

# 2 3 3 4 6 8 