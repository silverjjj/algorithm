'''

정수 A => B
string(A * 2) + string(1)

너비 우선 탐색,
빈 배열
2가지를 이용해서 푼다.
'''


def main():
    A,B = map(int,input().split())
    q = [A]
    dict = {}
    dict[A] = 0
    while q:
        cur = q.pop(0)
        if cur > 1000000000:
            continue

        cnt = dict[cur]
        if cur == B:
            return cnt + 1

        if dict.get(cur*2) == None:
            dict[cur*2] = cnt + 1
            q.append(cur*2)

        next = int(str(cur) + "1")
        if dict.get(next) == None:
            dict[next] = cnt+1
            q.append(next)

    return -1

print(main())