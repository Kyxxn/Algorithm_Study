import sys
from typing import List
def main():
    n,m = map(int, input().split())

    board = [[[],[]]for _ in range(n+1)]

    for _ in range(m):
        x,y = map(int,input().split())
        board[x][1].append(y)
        board[y][0].append(x)


    cases = int(input().strip())

    tmp = []
    visited = []
    def dfs(V:int,version:int):
        nonlocal tmp
        nonlocal visited

        if V in visited:
            return board[V][version]
        
        visited.append(V)
        
        if board[V][version] == []:
            return [V]
        
        for node in board[V][version]:
            tmp = dfs(node,version)
            board[V][version] = list(set(board[V][version] + tmp))
        
        return tmp
    
    visited = []
    for i in range(1,n+1):
        tmp = []
        dfs(i,1)

    visited = []
    for i in range(1,n+1):
        tmp = []
        dfs(i,0)


    for _ in range(cases):
        v,w = map(int,input().split())
        if w in board[v][1]:
            print("-1")
        elif w in board[v][0]:
            print("1")
        else:
            print("0")
main()

'''
[[[], []], [[], [2, 3]], [[1], [3, 4]], [[1, 2], [4]], [[3, 2], []], [[], []]]
0           1             2              3              4             5

[[[], []], [[], [2, 3, 4]], [[1], [3, 4]], [[1, 2], [4]], [[1, 2, 3], []], [[], []]]
'''
