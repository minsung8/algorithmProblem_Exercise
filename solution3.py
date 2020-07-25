def solution(n, build_frame):

    answer = []

    for i in range(len(build_frame)):

        if build_frame[i][3] == 1:
            answer.append(build_frame[i][:3])
            if check(answer):
                continue
            else:
                answer = answer[:-1]

        elif build_frame[i][3] == 0:
            answer.pop(answer.index(build_frame[i][:3]))
            if check(answer):
                continue
            else:
                answer.append(build_frame[i][:3])

    answer = sorted(answer, key=lambda x : (x[0], x[1], x[2]))

    return answer

def check(answer):

    for i in range(len(answer)):

        if answer[i][2] == 0:
            if (answer[i][1] == 0) or ([answer[i][0] - 1, answer[i][1], 1] in answer) or ([answer[i][0], answer[i][1], 1] in answer) or ([answer[i][0], answer[i][1] - 1, 0] in answer):
                continue
            else:
                return False

        elif answer[i][2] == 1:
            if ([answer[i][0], answer[i][1] - 1, 0] in answer) or ([answer[i][0] + 1, answer[i][1] - 1, 0] in answer) or ([answer[i][0] - 1, answer[i][1], 1] in answer and [answer[i][0] + 1, answer[i][1], 1] in answer):
                continue
            else:
                return False

    return True
