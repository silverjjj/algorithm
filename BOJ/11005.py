N, B = map(int,input().split())
numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res = ''
while N != 0:
    res += numbers[N%B]
    N //= B
print(res[::-1])