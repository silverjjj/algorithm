'''
1. index가 증가할때마다 현재의 오일의 가격을 비교
2. flag(이전의 오일가격중 가장 낮은 오일가격) vs cost[idx] (현재의 오일가격) 을 비교하여
    낮은 오일 가격 * 거리 를 더해나가면 됨
'''
import sys
input = sys.stdin.readline

N = int(input())
distance = list(map(int,input().split()))
cost = list(map(int,input().split()))
flag = float('inf')
res = 0
for idx in range(N-1):
    if flag >= cost[idx]:
        flag = cost[idx]
    res += flag*distance[idx]
print(res)