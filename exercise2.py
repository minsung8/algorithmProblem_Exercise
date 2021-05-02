def solution(array):

    max_array = max(array)
    answer_list = []

    for i in range(len(array)):

        if array[i] == max_array:
            answer_list.append(-1)
        else:
            j = 0
            while True:
                print(i, answer_list)
                j += 1
                if i - j > -1 and array[i - j] > array[i]:
                    answer_list.append(i - j)
                    break
                if i + j < len(array) and array[i + j] > array[i]:
                    answer_list.append(i + j)
                    break
    return answer_list



print(solution([3, 5, 4, 1, 2]))
print(solution([1, 2, 3, 4, 5]))