import itertools

arr = list(map(int,input().split()))
nums = [0,1,2]
dict = {}
q = []

lst = list(itertools.combinations(nums, 2))
for a,b in lst:
    visit = [0] * 3
    visit[a] = 1
    visit[b] = 1
    tmp = [1,2,3]
    if arr[a] > arr[b]:
        tmp[a] = arr[a] - arr[b]
        tmp[b] = arr[b] * 2
    else:
        tmp[b] = arr[b] - arr[a]
        tmp[a] = arr[a] * 2

    for i in range(3):
        if not visit[i]:
            tmp[i] = arr[i]
    q.append(tmp[:])
ans = 0
while q:
    arr1 = q.pop(0)

    char = str(arr1[0]) + str(arr1[1]) + str(arr1[2])
    if dict.get(char):
        continue
    dict[char] = 1

    for a, b in lst:
        visit = [0] * 3
        visit[a] = 1
        visit[b] = 1
        tmp = [1, 2, 3]
        if arr1[a] > arr1[b]:
            tmp[a] = arr1[a] - arr1[b]
            tmp[b] = arr1[b] * 2
        else:
            tmp[b] = arr1[b] - arr1[a]
            tmp[a] = arr1[a] * 2

        for i in range(3):
            if not visit[i]:
                tmp[i] = arr1[i]
        if max(tmp) == min(tmp):
            ans = 1
            break
        q.append(tmp[:])
print(ans)