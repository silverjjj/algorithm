'''
징검다리 건너기

징검다리(stones)은 밟을때마다 1씩 줄어듬
0이되면 더이상 밟을수 없고, 디딤돌로 여러칸을 건너뛸수있다.
단, 다음밟을수 있는건 가장 가까운 돌로 이동(최대 k)
한명씩 건너야함

건널수 있는 사람의 명수를 기준으로 이분탐색을 수행하자
최소 0명부터 최대 200000000명까지 범위를 정해놓고
해당 범위에서 이분탐색을 수행

'''
def binaray_search(stones, k):
    left, right = 0, 200000000

    while left <= right:
        mid = (left + right) // 2
        flag = False
        cnt = 0
        for i in range(len(stones)):
            if stones[i] - mid <= 0:
                cnt += 1
            else:
                cnt = 0

            # cnt가 k개랑 같거나 크면 더이상 건널수 없다.
            if cnt >= k:
                flag = True
                break

        if flag is True:
            right = mid - 1
        else:
            left = mid + 1

    return left

def solution(stones, k):

    return binaray_search(stones, k)

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
solution(stones, k)