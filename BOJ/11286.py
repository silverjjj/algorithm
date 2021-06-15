import heapq, sys
input = sys.stdin.readline

def BOJ11286(N):
    hq = []
    for _ in range(N):
        num = int(input())
        if num != 0:
            heapq.heappush(hq,(abs(num),num))
        else:
            if len(hq) > 0:
                ans = heapq.heappop(hq)
                print(ans[1])
            else:
                print(0)

N = int(input())
BOJ11286(N)