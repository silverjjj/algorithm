import sys
input = sys.stdin.readline

def DFS(k,visit):
    global maxV
    if k == P:
        return
    maxV = max(maxV, sum(visit))
    for i in range(g[k]):
        if not visit[i]:
            visit[i] = 1
            DFS(k+1,visit)
            visit[i] = 0

G = int(input())
P = int(input())
g = [int(input()) for _ in range(P)]
visit = [0]*G
maxV = 0
DFS(0,visit)
print(maxV)