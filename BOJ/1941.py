d = ((1,0),(-1,0),(0,1),(0,-1))

def DFS(i,j):
    visited = [[0]*5 for _ in range(5)]
    for dx, dy in d:
        nx = i + dx
        ny = j + dy
        if 0<= nx < 5 and 0<= ny < 5 and not visited[nx][ny]:




arr = [list(str(input())) for _ in range(5)]
for i in range(5):
    for j in range(5):
        DFS(i,j)
for r in arr:
    print(r)