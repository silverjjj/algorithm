'''

1. arr 정렬
2. left = 0, right = N-1 시작
3. arr[left] + arr[right] 의 값이 x와 같으면 cnt + 1
                                x보다 작으면 left + 1
                                x보다 크면 right + 1

'''

import sys
input = sys.stdin.readline

def BOJ3273(N,arr,X):
    left, right = 0, N-1
    ans = 0
    while left < right:
        res = arr[left] + arr[right]
        if res == X:
            ans += 1
        if res > X:
            right -= 1
            continue
        left += 1
    return ans

N = int(input())
arr = list(map(int,input().split()))
X = int(input())
arr.sort()
print(BOJ3273(N,arr,X))