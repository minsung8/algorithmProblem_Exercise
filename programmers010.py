from collections import defaultdict

def solution(word, pages):

    word = word.lower()
    url_dic = defaultdict(list)
    link_dic = defaultdict(list)
    idx = 0
    # 1. url, 링크 찾기
    for page in pages:
        temp_s = ''
        temp_url = ''
        flag = False
        temp_cnt = 0
        for i in range(len(page)):
            if page[i:i+32] == '<meta property=\"og:url\" content=':
                temp_url = page[i:].split('"')[3]
                url_dic[temp_url].append(idx)
                idx += 1
            if page[i:i+6] == '<body>':
                flag = True

            if flag:
                temp_s += page[i]

            if page[i:i+8] == '<a href=':
                temp_cnt += 1
                temp_link = page[i:].split('"')[1]
                link_dic[temp_link].append(temp_url)

            if page[i:i+7] == '</body>':
                url_dic[temp_url].append(temp_s[6:].lower())
                break
        url_dic[temp_url].append(temp_cnt)
    
    score_dic = {}
    # 3. url 별 기본점수 
    for key in url_dic.keys():
        temp_s = url_dic[key][1]
        temp_cnt = 0
        for i in range(len(temp_s) - len(word) - 1):
            if i == 0 and temp_s[i:i + len(word)] == word and not temp_s[i + len(word)].isalpha():
                temp_cnt += 1
            elif i > 0 and temp_s[i:i + len(word)] == word and not temp_s[i + len(word)].isalpha() and not temp_s[i - 1].isalpha():
                temp_cnt += 1
            elif i + len(word) == len(temp_s) - 1 and temp_s[i:i + len(word)] == word and not temp_s[i - 1].isalpha():
                temp_cnt += 1
        score_dic[key] = temp_cnt

    # 4. url 별 링크점수
    answer_list = []
    for key in url_dic:
        answer_list.append([key,score_dic[key], url_dic[key][0]]) #[url, url_score, idx]
        for key2 in link_dic[key]:
            answer_list[-1][1] += score_dic[key2] / url_dic[key2][-1]
    answer_list = sorted(answer_list, key=lambda x: (x[1], -x[2]), reverse=True)
    return url_dic[answer_list[0][0]][0]

print(solution('blind', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\nblind</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution('Muzi', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
