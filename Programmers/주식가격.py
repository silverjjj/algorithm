def solution(prices):
    L = len(prices)
    answer = [0] * L
    stack = []
    for idx, num in enumerate(prices):
        print(stack)
        if len(stack) == 0:
            stack.append([idx,num])
        else:
            print(idx,num)
            while stack[-1][1] > num or not len(stack):
                idx2, num2 = stack.pop()
                answer[idx2] = L-1-idx
            stack.append([idx, num])
    while stack:
        idx2, num2 = stack.pop()
        answer[idx2] = L - 1 - idx2
    print(answer)
    return answer
prices = [1,2,3,2,3]
solution(prices)