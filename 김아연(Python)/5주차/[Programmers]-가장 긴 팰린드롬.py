"""
부분 문자열의 길이를 조절하면서 팰린드롬인지 검사 후 맞으면 끝에서 시작점을 뺀 길이 저장
"""

def solution(s):
    answer = 1
    for i in range(len(s)):  # 시작부분 조절
        for j in range(len(s), i, -1):  # 끝부분 조절
            word = s[i:j]  # 부분문자열
            if word == word[::-1]:
                answer = max(answer, j-i)
    return answer
            
    # answer = 0
    # word1 = ''
    # for i in s:
    #     word1 += i
    #     if word1 == word1[::-1]:
    #         answer = max(len(word1), answer)
    # word2 = ''
    # for j in s[::-1]:
    #     word2 += j
    #     if word2 == word2[::-1]:
    #         answer = max(len(word2), answer)
    # return 1 if len(s) == 1 else answer