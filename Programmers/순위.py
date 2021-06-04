'''
results의 각 배열은 A,B를 의미하고 A가 이긴것
[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]의 경우
4 > 3   4 > 2    3 > 2   1 > 2    2 > 5
'''
def updown(win,lose,n,num):
    arr = [0] * (n + 1)
    q = [num]
    while q:
        # cur선수가 이긴 선수를 q 배열에 push
        cur = q.pop(0)
        if not arr[cur]:
            arr[cur] = 1
            for next in win[cur]:
                q.append(next)

    q = [num]
    arr[num] = 0
    while q:
        # cur선수가 진 선수를 q 배열에 push
        cur = q.pop(0)
        if not arr[cur]:
            arr[cur] = 1
            for next in lose[cur]:
                q.append(next)

    # 결국 arr는 맨처음 들어온 num 선수와 이기거나 진 선수들에 대해 표시한 배열임
    return arr
def solution(n, results):
    answer=0
    # 이긴 선수, 진 선수 기준으로 딕셔너리 생성
    win = {i: [] for i in range(1,n+1)}
    lose = {i: [] for i in range(1,n+1)}
    for winner, loser in results:
        win[winner].append(loser)
        lose[loser].append(winner)

    # 순서대로 선수 입장
    for num in range(1, n + 1):
        arr = updown(win,lose,n,num)
        # arr의 합과 n(선수의 수)와 같으면 num의 경기 성적을 알수있다
        if sum(arr) == n:
            answer += 1
    return answer

n = 5
results = 	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
solution(n, results)