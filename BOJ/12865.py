"""
0/1 Knapsack 알고리즘 문제
"""
def BOJ_12865(N,K,arr):
    dp = [[0]*(K+1) for _ in range(N+1)]

    for i in range(1,N+1):
        weight = arr[i][0]
        value  = arr[i][1]
        for j in range(1,K+1):
            if j < weight:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], value + dp[i-1][j-weight])

    return dp[N][K]

N, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
arr.insert(0,[0,0])
print(BOJ_12865(N,K,arr))