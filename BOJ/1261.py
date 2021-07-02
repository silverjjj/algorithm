import sys,heapq
input = sys.stdin.readline

d = ((0,1),(1,0),(-1,0),(0,-1))

n,m = map(int,input().split())
mapping = [input() for _ in range(m)]

dist = [[0]*n for _ in range(m)]
hq = []
heapq.heappush(hq,[0,0,0])
dist[0][0] = 1
while hq:
    cnt, x, y = heapq.heappop(hq)
    if x == n-1 and y == m-1:
        print(cnt)
        break
    for dx, dy in d:
        nx,ny = x+dx, y+dy
        if 0<=nx<m and 0<= ny < n:
            if not dist[nx][ny]:
                dist[nx][ny] = 1
                if mapping[nx][ny] == '1':
                    heapq.heappush(hq,[cnt+1,nx,ny])
                else:
                    heapq.heappush(hq, [cnt, nx, ny])

# deque를 활용한 방법
from collections import deque

d = ((0,1),(1,0),(-1,0),(0,-1))

n,m = map(int,input().split())
mapping = [input() for _ in range(m)]

dist = [[-1] * n for _ in range(m)]
dist[0][0] = 0
q = deque()
q.append([0, 0,0])
while q:
    x, y, cnt = q.popleft()
    for dx, dy in d:
        nx,ny = x+dx, y+dy
        if 0<=nx<m and 0<= ny < n:
            if dist[nx][ny] == -1:
                if mapping[nx][ny] == '0':
                    q.appendleft([nx, ny, cnt])
                    dist[nx][ny] = cnt
                elif mapping[nx][ny] == '1':
                    q.append([nx, ny, cnt + 1])
                    dist[nx][ny] = cnt + 1

print(dist[m - 1][n - 1])
