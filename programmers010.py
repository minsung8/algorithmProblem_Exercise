from collections import defaultdict

def solution(word, pages):

    url_dic = defaultdict(list) # [index, str, link1, link2, ...]
    link_dic = defaultdict(list)
    idx = 0
    word = word.lower()

    for page in pages:
        url_idx = page.index('content=')
        temp_url = page[url_idx:].split('"')[1]
        url_dic[temp_url].append(idx)

        body_start_idx = page.index('<body>')
        body_end_idx = page.index('</body>')

        temp_str = page[body_start_idx + 6:body_end_idx]
        url_dic[temp_url].append(temp_str)
        temp_cnt = 0
        for i in range(len(temp_str) - 8):
            if temp_str[i:i+8] == '<a href=':
                temp_cnt += 1
                url_dic[temp_url].append(temp_cnt)
                temp_link = temp_str[i:].split('"')[1]
                link_dic[temp_link].append(temp_url)

        idx += 1

    score_dic = defaultdict(int)
    length = len(word)

    for key in url_dic.keys():
        temp_str = url_dic[key][1].lower()
        score_dic[key] = 0
        for i in range(len(temp_str) - length + 1):
            if temp_str[i:i + length] == word:
                if i == 0:
                    score_dic[key] += 1
                elif i > 0 and not temp_str[i - 1].isalpha():
                    if i + length < len(temp_str) and not temp_str[i + length].isalpha():
                        score_dic[key] += 1
                    elif i + length == len(temp_str):
                        score_dic[key] += 1
                else:
                    continue

    answer_list = []
    for key in url_dic:
        answer_list.append([key,score_dic[key], url_dic[key][0]]) #[url, url_score, idx]
        for key2 in link_dic[key]:
            answer_list[-1][1] += score_dic[key2] / url_dic[key2][-1]
    answer_list = sorted(answer_list, key=lambda x: (x[1], -x[2]), reverse=True)
    print(answer_list)
    return url_dic[answer_list[0][0]][0]



print(solution('blind', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\nblind</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution('Muzi', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
