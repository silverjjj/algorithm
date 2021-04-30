"""
투 포인터
start 점과 end 점을 기준으로 하여
리스트에서 특정값(M)을 찾아내서 해당 인덱스를 반환할수 있다
로직 1: start는 end보다 항상 같거나 작야아한다.
       end 값은 N(리스트의 크기)보다 항상 작거나 같아야한다
로직 2: start ~ end의 값이 M과 같을경우 cnt + 1 하고 end + 1 해줌
로직 3: start ~ end 값이 M보다 작을경우 end + 1 해줌
로직 4: start ~ end 값이 M보다 클경우 start + 1 해줌
위 로직을 통해 리스트에서 M의 값을 같도록 하는 범위의 갯수를 찾을수 있다.

"""

def BOJ2003(N,M,arr):
    start, end = 0, 1
    cnt = 0
    # 로직1
    while start <= end and end <= N:
        res = sum(arr[start:end])
        # 로직2
        if res == M:
            cnt += 1
            end += 1
        # 로직3
        elif res < M:
            end += 1
        # 로직4
        else:
            start += 1
    return cnt
N,M = map(int,input().split())
arr = list(map(int,input().split()))
print(BOJ2003(N,M,arr))