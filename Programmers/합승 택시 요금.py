import heapq
def Dijkstra(start, end):
    INF = float('inf')
    n = len(adj)
    dist = [INF] * (n+1)
    dist[start] = 0
    hq = [[0,start]]

    while hq:
        cur_w, cur = heapq.heappop(hq)

        if dist[cur] < cur_w:
            continue

        for next, next_w in adj[cur]:
            if dist[next] > dist[cur] + next_w:
                dist[next] = dist[cur] + next_w
                heapq.heappush(hq,[next_w,next])
    return dist[end]

def solution(n, s, a, b, fares):
    global adj
    ans = 0
    adj = { i : [] for i in range(1,n+1)}
    # adj = [[] for _ in  range(n+1)]
    for st, end, cost in fares:
        adj[st].append([end,cost])
        adj[end].append([st,cost])
    ans = Dijkstra(s, a) + Dijkstra(s, b)
    for idx in range(1,n+1):
        if s == idx:
            continue
        ans = min(ans , Dijkstra(s, idx) + Dijkstra(idx, a) + Dijkstra(idx, b))
    return ans

n,s,a,b = 6,4,6,2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))