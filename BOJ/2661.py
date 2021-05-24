def DFS(N,k,char):
    for i in range(1,len(char) // 2 +1):
        if char[-i:] == char[(-2*i):-i]:
            return False

    if k == N:
        print(char)
        return True

    for num in range(1,4):
        if DFS(N, k+1, char + str(num)):
            return True

def BOJ2661(N):
    DFS(N,0,"")


N = int(input())
BOJ2661(N)