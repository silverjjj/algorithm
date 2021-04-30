import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dist = [[0]*N for _ in range(N)]
dist[0][0] = 1
for i in range(N):
    for j in range(N):
        if not arr[i][j]:
            continue
        nx = i + arr[i][j]
        ny = j + arr[i][j]
        if 0<= nx < N:
            dist[nx][j] += dist[i][j]
        if 0<= ny < N:
            dist[i][ny] += dist[i][j]
print(dist[-1][-1])