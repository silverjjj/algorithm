N = int(input())
arr = list(map(int,input().split()))
dp = [0]*(N)

# dp[0] = 1
for i in range(N):
    print()
    for j in range(i+1):
        print(i, j)
        dp[i] = max(dp[i], dp[i-j] + arr[j])
    print(dp)