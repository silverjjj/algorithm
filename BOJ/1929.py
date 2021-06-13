'''
에라토스테네스의 체로 푸는방법
1. 소수를 판단할 범위만큼의 배열의 크기를 생성
'''

import sys
input = sys.stdin.readline
def BOJ1929():
    visit = [True] * (M+1)
    visit[1] = False
    for i in range(2,M+1):
        if visit[i]:
            for idx in range(i+i,M+1,i):
                visit[idx] = False

    for i in range(M+1):
        if visit[i] and i >= N:
            print(i)

N,M = map(int,input().split())
numbers = [num for num in range(N,M+1)]
BOJ1929()