import sys
input = sys.stdin.readline

def BOJ1987(N,arr):
    cnt = 0
    for num in arr:
        if num == 1:
            cnt += 1
            continue
        for idx in range(2, num):
            if num % idx == 0:
                cnt += 1
                break

    return N - cnt

N = int(input())
arr = list(map(int,input().split()))
print(BOJ1987(N,arr))