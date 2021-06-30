'''
이분 탐색 or 투포인터 문제

'''
def BOJ2470(N,arr):
    # 맨 왼쪽, 오른쪽 정의
    left,right = 0,N - 1
    minV = float('inf')
    ans1,ans2 = 0,0
    while left < right:
        # tmp = 왼 + 오른의 합
        tmp = arr[left] + arr[right]
        # tmp가 minV보다 작으면 갱신해줌
        if minV > abs(tmp):
            ans1,ans2 = arr[left], arr[right]
            minV = abs(tmp)
            if abs(tmp) == 0:
                break
        # tmp가 0보다 크면 right값을 줄여 tmp를 0에 가깝게해야함
        if tmp > 0:
            right -=1
        else:
            left += 1

    print(ans1,ans2)

N = int(input())
arr = sorted(list(map(int,input().split())))
BOJ2470(N,arr)
