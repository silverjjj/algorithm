import sys, heapq
input = sys.stdin.readline
N = int(input())
M = int(input())
adj = {i : [] for i in range(1,N+1)}
INF = float('inf')
dist = [INF] * (N+1)
visit = [False]*(N+1)
for _ in range(M):
    a,b,c = map(int,input().split())
    adj[a].append((b,c))
    adj[b].append((a, c))
hq = []
heapq.heappush(hq,(0,1))
res = 0
while hq:
    w, cur = heapq.heappop(hq)
    if visit[cur]:
        continue
    visit[cur] = True
    res += w
    for next, weight in adj[cur]:
        if dist[next] > weight and not visit[next]:
            dist[next] = weight
            heapq.heappush(hq,(weight,next))
print(res)
