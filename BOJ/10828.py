import sys
input = sys.stdin.readline
def BOJ10828():
    stack = []
    N = int(input())
    for _ in range(N):
        char = str(input())
        if char[:2] == 'pu':
            push ,num = char.split(" ")
            stack.append(int(num))
        elif char[:2] == 'po':
            if len(stack) == 0:
                print(-1)
            else:
                pop = stack.pop()
                print(pop)
        elif char[:2] == 'si':
            print(len(stack))
        elif char[:2] == 'to':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
        elif char[:2] == 'em':
            if len(stack) == 0:
                print(1)
            else:
                print(0)

BOJ10828()