'''
대문자로 변환하는 upper와 소문자로 변환하는 lower에 대해 묻는문제
'''
def solution(s):
    answer = ''
    L = len(s)
    for i in range(L):
        if i == 0 or s[i-1] == " ":
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    return answer

s = "3people unFollowed m e"
print(solution(s))

s = "for the last week"
print(solution(s))