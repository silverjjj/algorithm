
def BOJ11055(N, arr):
    dp = [0]*N
    dp[0] = arr[0]
    for i in range(1, N):
        maxV = 0
        for j in range(i):
            if arr[i] > arr[j]:
                maxV = max(maxV, dp[j])
        dp[i] = maxV + arr[i]

    return max(dp)

N = int(input())
arr = list(map(int,input().split()))
print(BOJ11055(N, arr))

'''

5
10 90 20 80 100
210

8
3 10 2 7 11 5 13 8
37

10
102 100 2 3 4 3 5 6 7 8
102

5
5 1 2 3 10
16
'''