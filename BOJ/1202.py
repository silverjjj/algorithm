import heapq, sys
input = sys.stdin.readline

def main():
    N, K = map(int,input().split())
    hq,bags = [], []
    for _ in range(N):
        M, V = (map(int,input().split()))
        heapq.heappush(hq,(M,V))
    for _ in range(K):
        bags.append(int(input()))

    # 가방 무게를 오름 차순으로 정렬
    bags.sort()

    res = 0
    candidate = []

    for bag in bags:
        # 가방 무게인 bag보다 작은 무게를 가진 보석들을 모두 candidate에 push함
        while hq and bag >= hq[0][0]:
            m,v = heapq.heappop(hq)
            # push 할때는 최대힙을 활용하기 위해 -을 붙여 절대값이 가장 큰 숫자를 앞으로 이동시킴
            heapq.heappush(candidate, -v)

        # 후보군 배열에 보석이 존재하면
        if candidate:
            # 가장 무거운 보석을 pop해서 res에 더해준다
            res -= heapq.heappop(candidate)

    return res

print(main())