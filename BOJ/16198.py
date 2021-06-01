






def BOJ16198(N,arr):
    

N = int(input())
arr = list(map(int, input().split()))
print(BOJ16198(N,arr))


# def DFS(target,n, res):
#     global maxV
#     if res > maxV:
#         maxV = res
#
#     for i in range(1,n-1):
#         res += (arr[i - 1] * arr[i + 1])
#         num = arr.pop(i)
#         DFS(target, n-1, res)
#         arr.insert(i,num)
#         res -= (arr[i - 1] * arr[i + 1])
#
# def BOJ16198(N,arr):
#     global maxV
#     maxV = 0
#     DFS(N-2,N,0)
#     return maxV
#
# N = int(input())
# arr = list(map(int, input().split()))
# print(BOJ16198(N,arr))