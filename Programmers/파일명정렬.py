'''
핵심 - isdigit()을 아느냐 모르나냐 ?
isdigit()은 숫자의 참거짓을 판단할때 사용됨
비슷한걸로
isalpha()가 있는데, 이건 알파벳인지를 판단함
'''

def solution(files):
    answer = []
    arr = []
    for j in range(len(files)):
        file = files[j]
        idx = 0
        head, number, tail = "", "", ""
        while idx < len(file):
            if not file[idx].isdigit():
                head += file[idx]
            else:
                while idx < len(file):
                    if file[idx].isdigit():
                        number += file[idx]
                        idx += 1
                        continue
                    break

                while idx < len(file):
                    tail += file[idx]
                    idx += 1
            idx += 1
        arr.append([head.lower(), int(number), tail,j])
    arr = sorted(arr, key = lambda x : [x[0],x[1]])

    for a,b,c,d in arr:
        answer.append(files[d])
    return answer


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))
files =['muzi1.txt', 'MUZI1.txt', 'amuzi2.txt', 'muzi1.TXT']
print(solution(files))
