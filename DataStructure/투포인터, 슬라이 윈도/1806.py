
def BOJ1806(N,S, arr):
    start, end = 0,0
    res = 0
    L = 100001
    while start <= end and end < N:
        if res >= S:
            L = min(L, end - start)
            res -= arr[start]
            start += 1
        else:
            res += arr[end]
            end += 1

    if L == 100001:
        return 0
    else:
        return L

N,S = map(int,input().split())
arr = list(map(int,input().split()))
print(BOJ1806(N,S, arr))