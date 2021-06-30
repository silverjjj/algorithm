# 다음과 같이 import를 사용할 수 있습니다.
# import math
def solution(garden):
    # 여기에 코드를 작성해주세요
    d = ((0,1),(0,-1),(1,0),(-1,0))
    ans = 0
    n = len(garden)
    visit = [[False]*n for _ in range(n)]
    q = []
    for i in range(n):
        for j in range(n):
            if garden[i][j]:
                q.append((i,j,0))
                visit[i][j] = True

    while q:
        x,y,cnt = q.pop(0)
        ans = max(cnt, ans)
        for dx,dy in d:
            nx = x + dx
            ny = y + dy
            if 0<= nx < n and 0<= ny < n and not visit[nx][ny]:
                visit[nx][ny] = True
                q.append((nx,ny,cnt + 1))
    return ans


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

garden2 = [[1, 1], [1, 1]]
ret2 = solution(garden2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")