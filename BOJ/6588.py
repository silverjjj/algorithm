import sys
input = sys.stdin.readline

def primary_num():
    visit = [True] * 1000001
    visit[1] = False
    for i in range(2,1000001):
        if visit[i]:
            for j in range(i+i, 1000001, i):
                visit[j] = False

    return visit

def BOJ6588():
    visit = primary_num()
    for _ in range(100000):
        num = int(input())
        if num == 0:
            return
        for idx in range(3, 1000001):
            if visit[num-idx] and (num-idx) % 2:
                if visit[idx] and idx % 2:
                    print(num,'=',idx,'+',num-idx)
                    break

BOJ6588()