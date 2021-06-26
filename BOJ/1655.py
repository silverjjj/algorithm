import heapq, sys
input = sys.stdin.readline
T = int(input())
minHeapq, maxHeapq = [], []
for tc in range(T):
    num = int(input())
    if len(minHeapq) == len(maxHeapq):
        heapq.heappush(minHeapq, (-num, num))
    else:
        heapq.heappush(maxHeapq, (num, num))

    # minHeapq, maxHeapq에 모두 값이 있고
    # minHeapq의 가장 큰값이 maxHeapq의 가장 작은값보다 클경우 swap 한다
    if len(minHeapq) and len(maxHeapq) and minHeapq[0][1] > maxHeapq[0][1]:
        minV = heapq.heappop(minHeapq)[1]
        maxV = heapq.heappop(maxHeapq)[1]
        heapq.heappush(minHeapq, (-maxV, maxV))
        heapq.heappush(maxHeapq, (minV, minV))
    print(minHeapq[0][1])