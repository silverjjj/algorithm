def solution(rows, columns, queries):
    answer = []
    mapping = [[0]*columns for _ in range(rows)]
    num = 0
    for i in range(rows):
        for j in range(columns):
            num += 1
            mapping[i][j] = num

    for querie in queries:
        sx,sy,ex,ey = querie[0]-1,querie[1]-1,querie[2]-1,querie[3]-1
        i,j = 0,0
        tmp = []
        cur = mapping[sx][sy + j]
        while sy + j + 1 <= ey:
            j += 1
            next = mapping[sx + i][sy + j]
            mapping[sx + i][sy + j] = cur
            cur = next
            tmp.append(cur)

        while sx + i + 1 <= ex:
            i += 1
            next = mapping[sx + i][sy + j]
            mapping[sx + i][sy + j] = cur
            cur = next
            tmp.append(cur)
        while sy + j - 1 >= sy:
            j -= 1
            next = mapping[sx + i][sy + j]
            mapping[sx + i][sy + j] = cur
            cur = next
            tmp.append(cur)
        while sx + i - 1 >= sx:
            i -= 1
            next = mapping[sx + i][sy + j]
            mapping[sx + i][sy + j] = cur
            cur = next
            tmp.append(cur)

        answer.append(min(tmp))

    return answer



rows, columns, queries = 6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))

rows, columns, queries = 3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
print(solution(rows, columns, queries))

rows, columns, queries = 100,97,[[1,1,100,97]]
print(solution(rows, columns, queries))

