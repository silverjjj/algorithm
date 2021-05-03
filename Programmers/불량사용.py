"""
불량사용자 - DFS활용문제

"""
def compare(char1, char2):
    if len(char1) == len(char2):
        for k in range(len(char1)):
            if not (char1[k] == char2[k] or char1[k] == "*" or char2[k] == "*"):
                return False
    else:
        return False
    return True

def DFS(depth):
    if depth == len(arr):
        res.append("".join(sorted(tmp)))
    else:
        for num in arr[depth]:
            if num not in tmp:
                tmp.append(num)
                DFS(depth+1)
                tmp.pop()

def solution(user_id, banned_id):
    global answer, arr, tmp, res
    answer = 0
    tmp, res = [], []
    arr = [[] for _ in range(len(banned_id))]
    for i in range(len(user_id)):
        for j in range(len(banned_id)):
            char1, char2 = user_id[i], banned_id[j]
            if compare(char1, char2):
                arr[j].append(str(i))
    DFS(0)
    return len(set(res))


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
solution(user_id, banned_id)