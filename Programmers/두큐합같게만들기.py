'''

pop : 첫번쨰 원소 추출
insert : 끝에 원소 추가
원소 합이 같도록


1. 두 큐


queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

queue1 = [3, 2, 7, 2, 4]
queue2 = [6, 5, 1]

queue1 = [2, 7, 2, 4]
queue2 = [6, 5, 1, 3]

queue1 = [2, 7, 2, 4, 6]
queue2 = [5, 1, 3]

queue1 = [7, 2, 4, 6]
queue2 = [5, 1, 3, 2]

queue1 = [7, 2, 4, 6, 5]
queue2 = [1, 3, 2]

queue1 = [2, 4, 6, 5]
queue2 = [1, 3, 2, 7]


1. 시간초과 발생
    => 투포인터 ???
66.7
'''
from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    target = (sum(queue1) + sum(queue2)) // 2
    cnt = 0
    if sum(queue1) == target:
        return cnt
    maxCnt = len(queue1) * 3

    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)

    while queue1 and queue2 and maxCnt >= cnt:
        if queue1_sum == target:
            return cnt

        elif queue1_sum > queue2_sum:
            num = queue1.popleft()
            queue2.append(num)
            queue1_sum -= num
            queue2_sum += num
            cnt += 1
        elif queue1_sum < queue2_sum:
            num = queue2.popleft()
            queue1.append(num)
            queue1_sum += num
            queue2_sum -= num
            cnt += 1
    return -1

# queue1, queue2 = [3, 2, 7, 2], [4, 6, 5, 1]
# queue1, queue2 = [1, 2, 1, 2], [1, 10, 1, 2]
queue1, queue2 = [1, 1],[1, 5]

print(solution(queue1, queue2))