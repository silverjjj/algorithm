'''
그리드로 푼 문제임
students에서 큰 값을 기준으로 sort하여 수행함
'''
import sys
input = sys.stdin.readline

def BOJ9676(N, M, students):
    students.sort(key = lambda x:x[1])
    ans = [0]*(N+1)
    for st, end in students:
        for idx in range(st,end+1):
            if not ans[idx]:
                ans[idx] = 1
                break
    return sum(ans)

T = int(input())
for _ in range(T):
    N, M  = map(int,input().split())
    students = [list(map(int,input().split())) for _ in range(M)]
    print(BOJ9676(N,M,students))