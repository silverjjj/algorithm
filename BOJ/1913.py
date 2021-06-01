def find_num(x,y,num):
    global resX,resY
    if K == num:
        resX,resY = x+1, y+1

def up(x,y,num,M):
    for _ in range(M):
        num += 1
        x -= 1
        visit[x][y] = num
        find_num(x, y, num)
    return x,y,num

def right(x,y,num,M):
    for _ in range(M):
        num += 1
        y += 1
        visit[x][y] = num
        find_num(x, y, num)
    return x, y, num

def down(x, y, num, M):
    for _ in range(M):
        num += 1
        x += 1
        visit[x][y] = num
        find_num(x, y, num)
    return x,y,num

def left(x, y, num, M):
    for _ in range(M):
        num += 1
        y -= 1
        visit[x][y] = num
        find_num(x, y, num)
    return x,y,num

N = int(input())
K = int(input())
resX,resY = -1,-1
visit = [[0]*N for _ in range(N)]

cnt = 0
x,y = N//2, N//2
num = 1
visit[x][y] = num
while True:
    cnt += 1
    if N <= cnt:
        break
    x,y,num = up(x,y,num,cnt)
    x,y,num = right(x,y,num,cnt)

    cnt += 1
    if N <= cnt:
        break
    x, y, num = down(x, y, num, cnt)
    x, y, num = left(x, y, num, cnt)

x,y,num = up(x,y,num,cnt-1)
for r in visit:
    for number in r:
        print(number, end=" ")
    print()
print(resX, resY)