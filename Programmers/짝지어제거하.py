def solution(s):
    stack = ['0']
    for char in s:
        if stack[-1] == char:
            stack.pop()
        elif stack[-1] != char:
            stack.append(char)

    if len(stack) == 1:
        return 1
    else:
        return 0
s = 'cdcd'
print(solution(s))