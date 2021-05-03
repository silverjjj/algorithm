"""
순열, 완전탐색으로 풀었음
약 1시간 걸림
"""
# def perm(k):
#     if k == L:
#         tr.append(sign[:])
#         return
#     else:
#         for i in range(k,L):
#             sign[i], sign[k] = sign[k], sign[i]
#             perm(k+1)
#             sign[i], sign[k] = sign[k], sign[i]
#
# def find(cals, expressions):
#     for cal in cals:
#         idx = 0
#         arr = []
#         while True:
#             if idx == len(expressions):
#                 expressions = arr[:]
#                 if len(expressions) == 1:
#                     res.append(abs(expressions[0]))
#                 break
#             if expressions[idx] == cal:
#                 if expressions[idx] == "-":
#                     tmp = arr[-1] - expressions[idx+1]
#                     arr[-1] = tmp
#                 elif expressions[idx] == "+":
#                     tmp = arr[-1] + expressions[idx+1]
#                     arr[-1] = tmp
#                 elif expressions[idx] == "*":
#                     tmp = arr[-1] * expressions[idx+1]
#                     arr[-1] = tmp
#                 idx += 1
#             else:
#                 arr.append(expressions[idx])
#             idx += 1
#
# def solution(expression):
#     global tr, L, sign, res
#     sign, expressions = [], []
#     chars = ""
#     for char in expression:
#         if char in ("-","+","*"):
#             sign.append(char)
#             expressions.append(int(chars))
#             expressions.append(char)
#             chars = ""
#         else:
#             chars += char
#
#     expressions.append(int(chars))
#     sign = list(set(sign))
#     L = len(sign)
#     tr, res = [], []
#     perm(0)
#     for cals in tr:
#         find(cals, expressions)
#     return max(res)


def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        print(a,b)
        for e in expression.split(a):
            print(e)
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)

expression = "100-200*300-500+20"
solution(expression)