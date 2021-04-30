import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
stack = []
ans = [0]*N
for idx in range(N-1,-1,-1):
    tower = arr[idx]
    while stack and stack[-1][0] < tower:
        num = stack.pop()
        ans[num[1]] = idx+1
    stack.append([tower,idx])
print(' '.join(list(map(str,ans))))