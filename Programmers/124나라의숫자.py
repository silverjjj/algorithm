def solution(n):
    answer = ''
    char = '124'
    while n > 0:
        n-=1
        answer = char[n%3] + answer
        n //= 3
    return answer

n = int(input())
print(solution(n))