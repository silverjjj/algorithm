'''
공유기 사이의 거리를 기준으로 이분탐색수행
예를 들면 거리 5이상으로 이동하면 총 몇개의 공유기를 설치하지?
        거리 3이상으로 이동하면 총 몇개의 공유기를 설치하지?
        이런식으로 하자
'''
import sys
input = sys.stdin.readline

def calc(distance):
    cnt = 1
    start = arr[0]
    for idx in range(1,N):
        if start+distance <= arr[idx]:
            cnt += 1
            start = arr[idx]
    return cnt

def BOJ2110(N,C,arr):
    left,right = 1, arr[-1]-arr[0]
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if calc(mid) >= C:
            left = mid + 1
            ans = max(mid,ans)
        else:
            right = mid - 1

    return ans

N,C = map(int,input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
print(BOJ2110(N,C,arr))