# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?isFullScreen=true

def activityNotifications(expenditure, d):
    # Write your code here
    answer = 0

    for i in range(d, len(expenditure)):
        temp = sorted(expenditure[i - d:i])
        mid = _return_mid(temp)

        if mid * 2 <= expenditure[i]:
            answer += 1

    return answer

def _return_mid(_list):
    _len = len(_list)
    if _len % 2 != 0: return _list[_len // 2]
    return (_list[_len // 2 - 1] + _list[_len // 2]) / 2

print(activityNotifications([1, 2, 3, 4, 4], 4))    # 0


print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))    # 2
print(activityNotifications([10, 20, 30, 40, 50], 3))   # 1

