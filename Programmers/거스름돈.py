def BFS(n, money,res,arr):
    print(res)
    if sum(res) > n:
        return
    elif sum(res) == n:
        tmp = "".join(list(map(str,sorted(res))))
        arr.add(tmp)
        return
    for won in money:
        print("won", won)
        res.append(won)
        BFS(n, money, res,arr)
        res.pop()

def solution(n, money):
    arr = set([])
    BFS(n, money,[],arr)
    print(arr)
    return len(arr)
n = 5
money = [1,2,5]
solution(n, money)
