from collections import defaultdict

def solution(word, pages):

    url_dic = defaultdict(list) # [index, str, link1, link2, ...]
    link_dic = defaultdict(list)
    i = 0
    word = word.lower()
    
    # 1. 데이터 파싱
    for page in pages:
        page_list = page.split('\n')
        temp_url = ''
        temp_cnt = 0
        for p in page_list:
            if 'content="' in p:
                temp_url = p.split('"')[3]
                url_dic[temp_url].append(i)
                url_dic[temp_url].append('')
                i += 1
            if '<' not in p or '<a href' in p:
                url_dic[temp_url][1] += p.lower()
                if '<a href=' in p:
                    temp_link = p.split('"')[1]
                    link_dic[temp_link].append(temp_url)
                    temp_cnt += 1
        url_dic[temp_url].append(temp_cnt)

    # 2. 점수 계산
    score_dic = defaultdict(int)
    length = len(word)
    for key in url_dic:
        score_dic[key] = 0
        temp_str = url_dic[key][1]
        for i in range(len(temp_str)):
            if temp_str[i:i + length] == word:
                if i == 0:
                    score_dic[key] += 1
                elif i > 0 and not temp_str[i - 1].isalpha() and not temp_str[i + length].isalpha():
                    score_dic[key] += 1
                else:
                    continue
    
    answer_list = []
    for key in url_dic:
        answer_list.append([key,score_dic[key], url_dic[key][0]])
        for key2 in link_dic[key]:
            answer_list[-1][1] += score_dic[key2] / url_dic[key2][-1]
    print(answer_list)
    # 3. 정답
    answer_list = sorted(answer_list, key=lambda x: (x[1], -x[2]), reverse=True)
    return url_dic[answer_list[0][0]][0]


print(solution('blind', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution('Muzi', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
