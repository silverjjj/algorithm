'''
정확도 성공
효율성 실패
이진탐색을 활용하여 효율성을 높일수 있음
차후 수정계획
'''
import itertools

def comb(infos):
    cases = []
    for num in range(5):
        arrs = itertools.combinations([0,1,2,3],num)
        for arr in arrs:
            case = ""
            for idx in range(4):
                if idx not in arr:
                    case += str(infos[idx])
                else:
                    case += "-"
            cases.append(case)
    return cases

def solution(info, query):
    ans = []
    dict = {}
    for line in info:
        a, b, c, d, e = line.split(" ")
        cases = comb([a, b, c, d])
        for case in cases:
            if dict.get(case) == None:
                dict[case] = [int(e)]
            else:
                dict[case].append(int(e))

    for val in dict.values():
        val.sort()

    for line in query:
        qry = [i for i in line.split() if i != 'and']
        qry_cnd = ''.join(qry[:-1])
        score = int(qry[-1])
        if qry_cnd in dict:
            data = dict[qry_cnd]
            if len(data) > 0:
                st, end = 0, len(data)
                while st != end and st != len(data):
                    mid = (st + end) // 2
                    if data[mid] >= score:
                        end = mid
                    else:
                        st = mid + 1
                ans.append(len(data)-st)
        else:
            ans.append(0)
    return ans

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
solution(info, query)