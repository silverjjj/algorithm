def solution(board, moves):
    answer = 0
    N = len(board)
    stack = []
    for move in moves:
        j = move - 1
        for i in range(N):
            if board[i][j]:
                if len(stack) >= 1 and stack[-1] == board[i][j]:
                    answer += 2
                    stack.pop(-1)
                else:
                    stack.append(board[i][j])
                board[i][j] = 0                break
    print(stack,answer)
    return answer
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board,moves)