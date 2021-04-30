def solution(numbers):
    answer = set([])
    L = len(numbers)
    for i in range(L):
        for j in range(i+1,L):
            answer.add(numbers[i] + numbers[j])
    answer = list(answer)
    answer.sort()
    return answer

numbers = [2,1,3,4,1]
print(solution(numbers))