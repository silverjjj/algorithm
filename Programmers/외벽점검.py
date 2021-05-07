'''
둘레 n미터
취약한 지점들을 확인
점검시간을 1시간으로 제한
최소한의 친구들을 투입하여 취약지점 점검

3 4 13 23 24
'''

import itertools

def calc(candidate, row):
    j, cnt = 0, 1
    # dist는 인덱스가 아닌 for문으로 한개씩 던져주고
    # weaks의 row는 인덱스로 접근한다.
    # candidate = [3,5,7], row = [1,3,4,9,10]일때
    for num in candidate:
        res = 0
        # res = 3 + row[0] 인 4로 시작해서 while문에서 4보다 큰 row 인덱스를 찾아낸다
        res += (num + row[j])
        while True:
            if j == len(row)-1:
                break
            # 4 >= row[1], 3 / 4 >= row[2], 4 / 4 >= row[3], 9 가되어 break
            if res >= row[j+1]:
                j += 1
            else:
                j+=1
                cnt += 1
                break

    answer.append(cnt)

def solution(n, weak, dist):
    global answer
    answer = []
    # 순열을 통해 모든 dist 후보 생성
    candidates = itertools.permutations(dist, len(dist))

    weaks = []
    tmp = weak[:]
    # weak의 모든 숫자가 처음이 되도록 하는 배열 생성
    # ex) n = 12일때, [1,5,6,10], [5,6,10,13], [6,10,13,17] ...
    for i in range(1, len(weak)):
        tmp = tmp[1:] + [tmp[0]+n]
        weaks.append(tmp)

    # 한개의 dist마다 weak의 모든 경우를 비교한다
    for candidate in candidates:  #j
        for row in weaks:   #i
            calc(candidate, row)

    if min(answer) > len(dist):
        return -1

    return min(answer)

n = 12
weak = [1,5,6,10]
dist = [1,2,3,4]
solution(n, weak, dist)