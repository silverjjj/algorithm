'''
투포인터 문제

1. end에 1씩 더하면서 0 ~ end 까지의 합(res)을 더해감
2. res가 S보다 클경우 가장 짧은 길이(minV)를 구한 뒤, 합(res)에서 가장 앞(start)에있는 값을 빼줌

'''
def BOJ1806(N,S,arr):
    start, end = 0,0
    res = 0
    minV = float('inf')
    while True:
        if res >= S:
            minV = min(minV, end - start)
            res -= arr[start]
            start += 1
        elif end == N:
            break
        else:
            res += arr[end]
            end += 1

    if minV == float('inf'):
        return 0
    else:
        return minV

N, S = map(int,input().split())
arr = list(map(int,input().split()))
print(BOJ1806(N,S,arr))