def solution(k, tangerine):
    cnt = dict.fromkeys(tangerine, 0)
    for i in tangerine:
        cnt[i] += 1
    value = sorted(list(cnt.values()),reverse = True)
    answer = 0
    total = 0
    for i in range(len(value)):
        total += value[i]
        answer += 1
        if k <= total:
            break
    return answer