def BOJ2003(N,M,arr):
    start, end = 0, 1
    cnt = 0
    # 로직1
    while start <= end and end <= N:
        res = sum(arr[start:end])
        # 로직2
        if res == M:
            cnt += 1
            end += 1
        # 로직3
        elif res < M:
            end += 1
        # 로직4
        else:
            start += 1
    return cnt
N,M = map(int,input().split())
arr = list(map(int,input().split()))
print(BOJ2003(N,M,arr))