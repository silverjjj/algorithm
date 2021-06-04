def solution(A,B):
    ans = 0
    A.sort()
    B.sort(reverse= True)
    for a,b in zip(A,B):
        ans += a*b
    return ans

A = [1,4,2]
B = [5,4,4]
print(solution(A,B))