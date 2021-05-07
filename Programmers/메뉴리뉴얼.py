'''

1. 2명 이상ㅇ손님으로부터 주문된 단푼메뉴 조합
가장 많이 주문한 단품메뉴를 구성

'''
import itertools
def calc():
    maxV = max(dict.values())
    if maxV < 2:
        return
    for key, value in dict.items():
        if value == maxV:
            ans.append(key)

def sortedArr(arr):
    for row in arr:
        row = list(row)
        char = "".join(row)
        if dict.get(char) == None:
            dict[char] = 1
        else:
            dict[char] += 1

def solution(orders, course):
    global tr, dict, ans
    ans = []
    for num in course:
        dict = {}
        for order in orders:
            arr = itertools.combinations(sorted(order), num)
            sortedArr(list(arr))
        if len(dict) > 0:
            calc()

    ans.sort()
    return ans

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
solution(orders, course)