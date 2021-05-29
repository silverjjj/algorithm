import sys
from collections import deque
input = sys.stdin.readline

d = ((0,1),(0,-1),(1,0),(-1,0)) # 동서남북

def BOJ16197(N,M,mapping):
    coins = deque([])
    coin = []
    for i in range(N):
        for j in range(M):
            if mapping[i][j] == 'o':
                coin.append(i)
                coin.append(j)
    coin.append(0)
    coins.append(coin)

    while coins:
        x1,y1,x2,y2,cnt = coins.popleft()
        if cnt >= 10:
            return -1

        for dx,dy in d:
            nx1 = x1 + dx
            ny1 = y1 + dy
            nx2 = x2 + dx
            ny2 = y2 + dy

            # 둘다 내부이동
            if 0 <= nx1 < N and 0 <= ny1 < M and 0 <= nx2 < N and 0 <= ny2 < M:

                if mapping[nx1][ny1] == "#" and mapping[nx2][ny2] == "#":
                    continue

                if mapping[nx1][ny1] == "#":
                    nx1,ny1 = x1,y1

                if mapping[nx2][ny2] == "#":
                    nx2, ny2 = x2, y2

                coins.append((nx1,ny1,nx2,ny2,cnt+1))

            elif (0 <= nx1 < N and 0 <= ny1 < M) or (0 <= nx2 < N and 0 <= ny2 < M):
                return cnt+1

            else:
                continue
    return -1

N,M = map(int,input().split())
mapping = [list(str(input())) for _ in range(N)]
print(BOJ16197(N,M,mapping))