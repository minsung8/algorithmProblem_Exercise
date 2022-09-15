# https://www.hackerrank.com/challenges/two-pluses/problem?isFullScreen=true


def twoPluses(grid):
    answer = 0

    # padding
    temp = [["0"] * (len(grid) + 2)]
    for i in range(len(grid)):
        temp.append( ['0'] + list(grid[i]) + ['0'] )
    temp.append(["0"] * (len(grid) + 2))
    
    for i in range(1, len(temp) - 1):
        for j in range(1, len(temp[0]) - 1):
            
            r = 0
            while temp[i + r][j] == "G" and temp[i - r][j] == "G" and temp[i][j + r] == "G" and temp[i][j - r] == "G":
                temp[i + r][j] = temp[i - r][j] = temp[i][j + r] = temp[i][j - r] = "g"
                for I in range(1, len(temp) - 1):
                    for J in range(1, len(temp[0]) - 1):
                        R = 0

                        while temp[I + R][J] == "G" and temp[I - R][J] == "G" and temp[I][J + R] == "G" and temp[I][J - R] == "G":
                            answer = max(answer, (4 * r + 1) * (4 * R + 1) )
                            R += 1
                r += 1

            r=0
            while temp[i + r][j] == "g" and temp[i - r][j] == "g" and temp[i][j + r] == "g" and temp[i][j - r] == "g":
                temp[i + r][J] = temp[i - r][j] = temp[i][j + r] = temp[i][j - r] = "G"
                r+=1
    return answer

print(twoPluses(['GGGGGG', 'GBBBGB', 'GGGGGG', 'GGBBGB', 'GGGGGG']))    # 5
print(twoPluses(['BGBBGB', 'GGGGGG', 'BGBBGB', 'GGGGGG', 'BGBBGB', 'BGBBGB']))    # 25

print(twoPluses([
'GGGGGGG',
'BGBBBBG',
'BGBBBBG',
'GGGGGGG',
'GGGGGGG',
'BGBBBBG']))   


print(twoPluses(
['GGGGGGGG',
 'GBGBGGBG',
 'GBGBGGBG',
 'GGGGGGGG',
 'GBGBGGBG',
 'GGGGGGGG',
 'GBGBGGBG',
 'GGGGGGGG']
))
