from collections import defaultdict

def solution(k, tangerine):
    board = defaultdict(int)
    answer = 0
    for i in tangerine:
        board[i] += 1
        
    for i in sorted(board.values(),reverse=True):
        k -= i
        answer += 1
        if k <= 0:
            break

    return answer


k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
result = 3

print(solution(k,tangerine))