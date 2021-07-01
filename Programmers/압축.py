'''
KAKAO in

K => 11
KA를 27로 등록
A => 1
AK를 28로 등록
KA => 27
0를 29로 등록
0 => 15 출력

사전에 등록된 가장 긴 문자열 w를 찾는다
있다면 w 번호를 출력한뒤 입력에서 w 제거
입력에서 처리 되지 않은 다음 글자가 남아 있다면 w+c 등록

'''

def solution(msg):
    ans = []
    # 1. dict 생성
    dict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,
            'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,
            'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    l = len(msg)
    number = 27
    visit = [0]*l
    # 2. idx = 0 ~ len(msg)
    for i in range(len(msg)):
        if visit[i]:
            continue

        # 3. idx 부터 시작해서 len(msg) 까지 긴 문자열 w가 있나 찾자
        for j in range(i+1,len(msg)+1):

            # 마지막 까지 도달하면 더이상 찾지 않고 끝낸다.
            if j == l:
                char = dict[msg[i:j+1]]
                ans.append(char)
                for k in range(i,j):
                    visit[k] = 1

            # 4. 가장 큰 문자열을 w의 번호를 출력한뒤, w + c를 등록
            if not dict.get(msg[i:j+1]):
                dict[msg[i:j+1]] = number
                number += 1
                char = dict[msg[i:j]]
                ans.append(char)
                for k in range(i,j):
                    visit[k] = 1
                break
    return ans

msg = 'KAKAO'
print(solution(msg))
msg = 'TOBEORNOTTOBEORTOBEORNOT'
print(solution(msg))
msg = 'ABABABABABABABAB'
print(solution(msg))