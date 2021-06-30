H,W = map(int,input().split())
arr = list(map(int,input().split()))
res = 0
for i in range(W):
    print(arr[i:], arr[:i+1], arr[i])
    res += min(max(arr[i:]), max(arr[:i+1]))-arr[i]
    print(res)