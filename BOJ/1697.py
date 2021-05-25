from collections import deque

def BOJ1697(N, K):
    maxV = 100001
    visit = [False] * maxV
    dq = deque([(N, 0)])
    while dq:
        cur, cnt = dq.popleft()
        if cur == K:
            return cnt
        if 0 <= cur * 2 < maxV and not visit[cur * 2]:
            dq.append((cur * 2, cnt + 1))
            visit[cur * 2] = True

        if 0 <= cur - 1 < maxV and not visit[cur - 1]:
            dq.append((cur - 1, cnt + 1))
            visit[cur - 1] = True

        if 0 <= cur + 1 < maxV and not visit[cur + 1]:
            dq.append((cur + 1, cnt + 1))
            visit[cur + 1] = True

N, K = map(int, input().split())
print(BOJ1697(N, K))