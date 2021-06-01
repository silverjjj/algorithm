
def BOJ16968(chars):
    if chars[0] == 'd':
        ans = 10
    else:
        ans = 26

    for i in range(1,len(chars)):
        if chars[i] == 'd':
            if chars[i-1] == 'd':
                ans *= 9
            else:
                ans *= 10
        else:
            if chars[i - 1] == 'c':
                ans *= 25
            else:
                ans *= 26

    return ans
N = input()
if N:
    print(BOJ16968(N))
else:
    print(1)