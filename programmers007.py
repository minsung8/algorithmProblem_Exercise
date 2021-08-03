def solution(enroll, referral, seller, amount):
    answer = {}
    ref_dic = {}

    for i in range(len(enroll)):
        answer[enroll[i]] = 0
        ref_dic[enroll[i]] = referral[i]
    
    for i in range(len(seller)):
        temp_amount = amount[i] * 100
        temp = seller[i]

        while True:
            if len(str(temp_amount)) == 1:
                answer[temp] += temp_amount
                break
            temp_amount2 = int(temp_amount * 0.1)
            answer[temp] += temp_amount - temp_amount2
            temp_amount = temp_amount2
            temp = ref_dic[temp]

            if temp == "-":
                break
    
    result = []
    for i in range(len(enroll)):
        result.append(answer[enroll[i]])
    return result


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
                , ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
                , ["young", "john", "tod", "emily", "mary"]
                , [12, 4, 2, 5, 10]
                ))
