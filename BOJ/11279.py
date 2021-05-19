import heapq, sys
input = sys.stdin.readline

def main():
    N = int(input())
    hq = []
    for _ in range(N):
        num = int(input())
        if num == 0:
            if len(hq) == 0:
                print(0)
            else:
                n = heapq.heappop(hq)
                print(n[1])
        else:
            heapq.heappush(hq, (-num,num))
main()