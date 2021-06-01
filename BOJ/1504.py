import heapq, sys
input = sys.stdin.readline

def Dijkstra(st):
    dist = [INF] * (N + 1)
    dist[st] = 0
    hq = []
    heapq.heappush(hq, (0, st))
    while hq:
        w, cur = heapq.heappop(hq)
        for next, wight in adj[cur]:
            if dist[next] > wight + w:
                dist[next] = wight + w
                heapq.heappush(hq, (wight + w, next))
    return dist

def BOJ1504():
    from_1 = Dijkstra(1)
    from_st = Dijkstra(start)
    from_end = Dijkstra(end)

    case1 = from_1[start] + from_st[end] + from_end[N]
    case2 = from_1[end] + from_st[N] + from_end[start]
    res = min(case1, case2)
    if INF > res:
        return res
    else:
        return -1

N,E = map(int,input().split())
adj = {i : [] for i in range(1,N+1)}
for _ in range(E):
    a,b,c = map(int,input().split())
    adj[a].append([b,c])
    adj[b].append([a, c])
start, end = map(int,input().split())
INF = float('inf')
print(BOJ1504())