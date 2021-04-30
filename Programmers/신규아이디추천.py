def solution(new_id):
    answer = '+'
    special = ('-','_')
    for i in range(len(new_id)):
        char = new_id[i]
        if (char in special) or char.isdigit() or char.islower():
            answer += char
        elif char.isupper():  # 대문자냐?
            answer += char.lower()
        elif char == ".":
            if answer[-1] == ".":
                continue
            else:
                answer += char
    answer = answer[1:]
    #  4단계
    if answer[0] == ".":
        answer = answer[1:]
    if len(answer) >= 1 and answer[-1] == ".":
        answer = answer[:-1]
    # 5단계
    if len(answer) == 0:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    return answer

new_id = "abcdefghijklmn.p"
solution(new_id)