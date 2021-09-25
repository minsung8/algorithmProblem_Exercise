from collections import defaultdict

def solution(word, pages):
    word = word.lower()
    url_dic = {}
    linked_dic = defaultdict(list)
    linked_cnt_dic = defaultdict(list)

    temp_s = ''

    # 1. 데이터 파싱
    for url in pages:
        temp = url.split('\n')
        for idx in temp:
            if "content=" in idx:
                temp_str = idx.split('"')
                for s in temp_str:
                    if "https" in s:
                        url_dic[s] = 0
                        temp_s = s
            
            if len(idx) > 0 and idx[0] != ' ' and idx[0] != '<':
                temp_str = idx.lower()
                temp_cnt = temp_str.count(word)
                url_dic[temp_s] += temp_cnt

            if len(idx) > 1 and idx[:2] == '<a':
                temp_link = idx.split('"')[1]
                linked_dic[temp_link].append(temp_s)
                linked_cnt_dic[temp_s].append(temp_link)

    answer_dic = []
    i = 0
    # 2. 점수 계산
    for key in url_dic.keys():
        temp_score = url_dic[key]
        for key2 in linked_dic[key]:
            temp_score += url_dic[key2] / len(linked_cnt_dic[key2])
        answer_dic.append([i, temp_score])
        i += 1

    # 3. answer return
    answer = sorted(answer_dic, key=lambda x : x[1])
    print(answer)
    return answer[0][0]


#print(solution('blind', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution('Muzi', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))