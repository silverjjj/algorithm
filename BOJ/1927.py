import heapq, sys
input = sys.stdin.readline
def BOJ1927():
    N = int(input())
    hq = []
    for _ in range(N):
        num = int(input())
        if num == 0:
            if len(hq) == 0:
                print(0)
            else:
                n = heapq.heappop(hq)
                print(n)
        else:
            heapq.heappush(hq,num)

BOJ1927()