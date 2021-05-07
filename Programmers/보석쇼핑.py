
def solution(gems):
    answer = []
    # 1. set으로 모든 보석을 찾는다
    newGems = set(gems)
    L = len(newGems)

    dict = {}
    for idx in range(len(gems)):
        if dict.get(gems[idx]) == None:
            dict[gems[idx]] = idx+1
        else:
            dict[gems[idx]] = idx+1

        if len(dict) == L:
            lst = list(dict.values())
            lst.sort()
            lst.insert(0,lst[-1]-lst[0])
            answer.append(lst)

    answer.sort(key=lambda x:[x[0], x[1]])

    return [answer[0][1],answer[0][-1]]

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
solution(gems)
