import sys
input = sys.stdin.readline

N = int(input())
Narr = list(map(int,input().split()))
M = int(input())
Marr = list(map(int,input().split()))

numbers = {}
for num in Narr:
    if numbers.get(num) is None:
        numbers[num] = 1
    else:
        numbers[num] += 1
numList = list(set(Narr))
numList.sort()
ans = []
for num in Marr:
    if numbers.get(num) is None:
        print(0, end = " ")
    else:
        print(numbers[num], end= " ")