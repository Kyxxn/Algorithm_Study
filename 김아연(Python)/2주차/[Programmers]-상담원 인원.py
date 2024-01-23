# 내 풀이(다른사람 풀이 참고)
from itertools import combinations_with_replacement

def solution(k, n, reqs):
    answer = 999999999  # 최소의 시간을 구해야 하므로 큰 수 저장
    start_end = {i:[] for i in range(1,k+1)}  # 유형별로 참가자들의 시작, 끝 시간을 넣을 딕셔너리
    comb = list(combinations_with_replacement([i for i in range(k)],r=n-k))  # 중복조합을 사용하여 n-k개의 선택에 대한 조합을 구함
    
    cases = []
    for case in comb:
        base = [1 for _ in range(k)]  # 최소 1명의 멘토를 저장하고 
        for c in case:
            base[c]+=1  # 각 경우에 맞는 자리에 한명씩 더한 뒤 
            
        cases.append(base) # 모든 경우의 수에 추가
    
    for s, e, t in reqs: 
        start_end[t].append([s,s+e]) # 시작, 끝시간 저장
    
    for case in cases:
        wait = 0  # 각 유형은 독립적이므로, 각 유형에 대한 대기시간의 합이 각각의 경우의 대기시간이다. 
        for i in range(k):
            p = sorted(start_end[i+1], key = lambda x:x[0]) # 시작시간을 기준으로 정렬
            mento_end_list = [0 for _ in range(case[i])] # 각 멘토의 상담 종료 시간을 저장하는 배열
            for s, e in p:  # s = 시작시간, e = 끝시간
                mento_end_list = sorted(mento_end_list) # 종료시간이 가장 이른 곳에 배치하기 위해
                if mento_end_list[0] <= s:  # 만약 종료시간이 다음 시작시간보다 작다면
                    mento_end_list[0] = e  # 그 다음 상담종료시간 저장
                else: 
                    tmp = mento_end_list[0] - s  # 대기시간
                    mento_end_list[0] = e + tmp  # 상담 종료시간 + 기다려야하는 시간
                    wait += tmp  # 대기시간 추가
            if wait > answer:
                break
        if wait < answer:
            answer = wait
        
    return answer