import sys

input = sys.stdin.readline

cases = int(input().strip())
for _ in range(cases):
    n = int(input().strip())
    lose = []

    board = [list(map(int,input().split())) for __ in range(n)]
    board.sort(key=lambda x: x[0])
    
    for i , case in enumerate (board):
        for j in range(i,n):
            if board[j] in lose:
                continue
            if board[j][1] > case[1]:
                lose.append(board[j])
                
    board.sort(key=lambda x: x[1])
    for i , case in enumerate (board):
        for j in range(i,n):
            if board[j] in lose:
                continue
            if board[j][0] > case[0]:
                lose.append(board[j])

    print(n - len(lose))
    

