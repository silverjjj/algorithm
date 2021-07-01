def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])

    # 1. m-1 * n-1 를 기준으로 한바퀴 돌면서 사각형을 찾아 해당 좌표를 set에 add한다
    while True:
        remove = set([])
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == '0':
                    continue
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    remove.add((i,j))
                    remove.add((i, j+1))
                    remove.add((i+1, j))
                    remove.add((i+1, j+1))

        # 2. set의 크기가 0이 될때까지 반복
        if len(remove) == 0:
            break

        for i,j in remove:
            board[i][j] = '0'
        # 3. 없애주는 remove 갯수 더해주기
        answer += len(remove)

        # 4. 없어진 부분 채우기
        for i in range(m-1,-1,-1):
            for j in range(n):
                if board[i][j] == '0':
                    add = 0
                    while i + add > 0:
                        add -= 1
                        if board[i+add][j] != '0':
                            char = board[i+add][j]
                            board[i][j] = char
                            board[i + add][j] = '0'
                            break

    return answer


m,n,board = 4,5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m, n, board))

m,n,board = 6,6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m, n, board))