'''

4개 지표,
MBTI
1번 : R T
2번 : C F
3번 : J M
4번 : A N


["AN", "CF", "MJ", "RT", "NA"]

1번 비동의 : A, 동의 : N
=> choices[i] : 5 약간 동의

(choices[i] - 4)  > 0 => N += 1 점

2번 비동의 : C, 동의 : F
..

5번 비동의 : N, 동의 : A
=> choices[i] : 5 약간 동의

choices[i] - 4 > 0 ==> A += 1점

같은지표에서 점수가 같으면 사전순으로 빠른걸로 선택

'''
def solution(survey, choices):
    dict = {'RT' : {'R' : 0, 'T' :0},
            'CF': {'C': 0, 'F': 0},
            'JM': {'J': 0, 'M': 0},
            'AN': {'A': 0, 'N': 0}}

    answer = ''

    l = len(choices)
    for i in range(l):
        a, b = survey[i][0], survey[i][1]
        num = choices[i]
        point = 0
        char = [a, b]
        char.sort()
        charSort =''.join(char)
        if (num - 4 > 0):    #  동의 => 오른쪽점수 할당 b
            point = num - 4
            dict[charSort][b] += point
        elif (num - 4 < 0):  # 비동의  = > a
            point = 4 - num
            dict[charSort][a] += point

    for key, val in dict.items():
        tmp = list(val.values())
        if tmp[0] == tmp[1]:
            answer += key[0]
            continue
        else:
            maxV = max(list(val.values()))

        for key2, value2 in val.items():
            if value2 == maxV:
                answer += key2

    return answer

# survey = ["AN", "CF", "MJ", "RT", "NA"]
# choices = [5, 3, 2, 7, 5]

survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]
solution(survey, choices)