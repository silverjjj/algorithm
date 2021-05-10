def BOJ2512(N, local,M):
    left, right = 0, max(local)
    while left <= right:
        mid = (left + right) // 2
        res = 0
        for cost in local:
            if mid <= cost:
                res += mid
            else:
                res += cost
        if res <= M:
            left = mid + 1
        else:
            right = mid - 1

    return right


N = int(input())
local = list(map(int,input().split()))
M = int(input())
print(BOJ2512(N, local,M))