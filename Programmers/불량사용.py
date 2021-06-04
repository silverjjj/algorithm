"""
불량사용자 - DFS활용문제

"""
def compare(char1, char2):
    # 길이 비교
    if len(char1) == len(char2):
        for k in range(len(char1)):
            # 문자 비교
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

    # 2중 for문으로 user_id와 banned_id를 비교함
    for i in range(len(user_id)):
        for j in range(len(banned_id)):
            char1, char2 = user_id[i], banned_id[j]
            if compare(char1, char2):
                # arr의 j는 banned_id의 idx를 의미함
                # arr[j]의 내부값은 user_id의 idx 의미함
                arr[j].append(str(i))

    DFS(0)
    print(res)
    return len(set(res))


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
solution(user_id, banned_id)