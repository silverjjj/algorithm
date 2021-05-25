import heapq

def BOJ1966(N,M,arr,idxList):
    cnt = 0
    while arr:
        if max(arr) == arr[0]:
            if idxList[0] == M:
                return cnt + 1
            else:
                arr.pop(0)
                idxList.pop(0)
                cnt += 1
        else:
            arr.append(arr.pop(0))
            idxList.append(idxList.pop(0))

T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    idxList = [i for i in range(N)]
    print(BOJ1966(N,M,arr,idxList))