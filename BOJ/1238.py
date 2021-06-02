import heapq, sys
input = sys.stdin.readline

def dijkstra(st,adj):
    INF = float('inf')
    dist = [INF] * (N+1)
    dist[st] = 0
    hq = [[0,st]]
    while hq:
        w, cur = heapq.heappop(hq)

        # 현재 위치인 cur 의 모든 인접한 정점을 for문으로 돌린다.
        for next, weight in adj[cur]:
            # 기존에 정의된 최소거리값보다 더 작은경우 갱신해준다.
            if dist[next] > weight + w:
                dist[next] = weight + w
                heapq.heappush(hq,[dist[next], next])
    return dist

N,M,X = map(int,input().split())
adj1 = {i : [] for i in range(1, N+1)}
adj2 = {i : [] for i in range(1, N+1)}
# 인접 리스트를 생성해준다.
for _ in range(M):
    a,b,c = map(int,input().split())
    adj1[a].append([b,c])
    adj2[b].append([a, c])

# X를 시작으로 하여 모든 최소거리 구한다
start_X = dijkstra(X,adj1)
# X를 도착으로 하여 모든 최소거리를 구한다.
start_all = dijkstra(X,adj2)
ans = max([i+j for i,j in zip(start_X[1:], start_all[1:])])
print(ans)
