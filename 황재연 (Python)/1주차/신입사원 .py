import sys

input = sys.stdin.readline

cases = int(input().strip())
for _ in range(cases):
    n = int(input().strip())
    lose = 0

    board = [list(map(int,input().split())) for __ in range(n)]
    board.sort(key=lambda x: (x[1],x[0]))
    
    x = n

    for i, val in enumerate(board):
        if val[0] <= x:
            x = val[0]
        else:
            lose += 1 
    print(n - (lose))