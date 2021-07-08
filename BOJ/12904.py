def BOJ12904(S,T):
    while True:
        if len(T) == len(S):
            if T == S:
                return 1
            else:
                return 0

        if T[-1] == 'B':
            T = T[:-1]
            T = T[::-1]
        else:
            T = T[:-1]

S = input()
T = input()
print(BOJ12904(S,T))