k = int(input())
tangerine = sorted(list(map(int, input().split())))

tangerine_count = []
count = 1
ans = 0

for i in range(1, len(tangerine)):
    if tangerine[i-1] == tangerine[i]:
        count += 1
    else:
        tangerine_count.append(count)
        count = 1

tangerine_count.append(count)

sorted_tangerine_count = sorted(tangerine_count, key=lambda x: -x)

total_count = 0

for i in range(len(sorted_tangerine_count)):
    total_count += sorted_tangerine_count[i]

    if total_count >= k:
        ans = i+1
        break

print(ans)

"""
# 프로그래머스 제출본
def solution(k, tangerine):
    # tangerine 오름차순 정렬
    tangerine = sorted(tangerine)

    tangerine_count = []
    count = 1
    answer = 0

    for i in range(1, len(tangerine)):
        if tangerine[i-1] == tangerine[i]:
            count += 1
        else:
            tangerine_count.append(count)
            count = 1

    # 마지막 요소의 개수를 처리
    tangerine_count.append(count)
    
    # tangerine_count 내림차순 정렬
    sorted_tangerine_count = sorted(tangerine_count, key=lambda x: -x)
    
    # 상자에 담을 최소 종류 개수 구함
    total_count = 0
    for i in range(len(sorted_tangerine_count)):
        total_count += sorted_tangerine_count[i]
        if total_count >= k:
            answer = i+1
            break
    return answer
"""