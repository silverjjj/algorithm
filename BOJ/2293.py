import sys
input = sys.stdin.readline
N, K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
dp = [0]*(K+1)
dp[0] = 1
for coin in coins:
    for idx in range(K+1):
        if idx - coin >= 0:
            dp[idx] += dp[idx-coin]
print(dp[K])
'''
    1 2 3 4 5 6 7 8 9 10원
1   1 1 1 1 1 1 1 1 1 1 
2   0 1 1 2 2 3 3 4 5 5
5   0 0 0 0 1 1 2 2 3 4

'''