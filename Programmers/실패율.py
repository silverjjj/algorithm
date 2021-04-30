def solution(N, stages):
    ans = [[i, 0] for i in range(N+1)]
    dict = {}
    L = len(stages)
    for stage in stages:
        if not dict.get(stage):
            dict[stage] = 1
        else:
            dict[stage] += 1
    for stage, cnt in (sorted(dict.items())):
        if stage == N+1:
            continue
        ans[stage] = [stage,cnt/L]
        L -= cnt
    ans.pop(0)
    res = [i for i,j in sorted(ans, key=lambda x: -x[1])]
    return res

stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 5
solution(N, stages)