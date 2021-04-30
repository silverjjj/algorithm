def solution(s):
    answer = []
    arr,tmp,tmp2,dict = [],"",[],{}
    flag = False
    for char in s[1:-1]:
        if flag:
            if char != "," and char != "}":
                tmp += char
            if char == "," or char == "}":
                tmp2.append(tmp)
                tmp = ""
        if char == "{":
            flag = True
            continue
        elif char == "}":
            flag = False
            arr.append(tmp2[:])
            tmp2 = []

    arr.sort(key = lambda x : len(x))
    for nums in arr:
        for num in nums:
            if dict.get(int(num)) == None:
                dict[int(num)] = True
                answer.append(int(num))
    print(answer)
    return answer
s ="{{20,111},{111}}"
solution(s)