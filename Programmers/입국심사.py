'''
이분탐색문제
n명의 사람
times = 각 심사관이 한명을 심사하는데 걸리는 시간
'''
def solution(n, times):
    # 최대 시간과 최소시간을 정의
    ans = 0
    left, right = 0,max(times) * n
    mid = (right + left) // 2
    while left <= right:
        person = 0
        # mid분일때 최대 몇명의 사람을 심사할수 있냐 ?
        for time in times:
            person += (mid // time)
            # n 명이상이면 for문 탈출
            if person > n:
                break
        # n명 이상 했으면 mid분이 많다는 뜻, ==> mid를 줄이고 ans = mid에 할당
        if person >= n:
            right = mid - 1
            ans = mid
        # n명 미만 했으면 시간을 더 늘려야함
        elif person < n:
            left = mid + 1
        mid = (right + left) // 2
    return ans
n = 6
times = [7,8]
solution(n, times)