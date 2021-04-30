N = int(input())
dist = [0] * (N + 1)
dist[1] = 1
if N >= 2:
    for i in range(2, N+1):
        dist[i] = dist[i-1] + dist[i-2]
print(dist[-1])