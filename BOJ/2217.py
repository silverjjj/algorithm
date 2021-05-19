import sys
input = sys.stdin.readline

def BOJ2217(N, rope):
    dist = [0]*N
    rope.sort()
    for i in range(N):
        dist[i] = rope[i]*(N-i)
    return max(dist)

N = int(input())
rope = [int(input()) for _ in range(N)]
print(BOJ2217(N, rope))