'''
프로그래머스 - 경주로 건설
1시간 25분걸림

격자는 1 or 0으로 채워짐
0 : 비어있음을 의미
1 : 채워져 있음

직선 도로 : 상 <-> 하 or 좌 <-> 우
코너 : 직선도로를 제외한 모든 도로
직선도로 => 100원
코너 ==> 500원

최소비용을 찾자!!
'''

from collections import deque

dx = [0,-1,1,0,0] # 1:상, 2:하, 3: 좌, 4: 우
dy = [0,0,0,-1,1]
passD = [0,2,1,4,3]

def solution(board):
    N = len(board)
    q = deque()
    # x좌표, y좌료, 방향, 비용 순서
    visited = {(0,0,1) : 0, (0,0,2) : 0, (0,0,3) : 0,(0,0,4) : 0}
    q.append([0,0,-1,0])
    minValue = float('inf')

    while q:
        x, y, preD, cost = q.popleft()
        for i in range(1,5):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not board[nx][ny]:
                if preD == -1:
                    nextCost = cost + 100
                elif preD == i:
                    nextCost = cost + 100
                else:
                    nextCost = cost + 600

                if x == N - 1 and y == N - 1:
                    minValue = min(minValue, cost)

                elif visited.get((nx,ny,i)) is None or visited.get((nx,ny,i)) > nextCost:     # 방문을 전혀안했다면 방문
                    visited[(nx,ny,i)] = nextCost
                    q.append((nx,ny,i,nextCost))
    return minValue


# board =[[0,0,0],[0,0,0],[0,0,0]]
board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
# board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
print(solution(board))