import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def main():
    num = int(input().strip())

    tree = defaultdict(list)

    for _ in range(num- 1):
        n, m, v = map(int, input().split())
        tree[n].append([m, v])
        tree[m].append([n, v])

    leafs = [leaf[0] for leaf in tree.items() if len(leaf[1]) == 1]
    discovered = []

    ans = [0]*(num+1)

    def dfs(V, value, check=False):
        nonlocal visited  # 방문한 노드
        nonlocal leafs
        nonlocal ans
        if (not check) and V in leafs:
            ans[V] = value

        visited.append(V)

        for i in tree[V]:
            if i[0] in visited:
                continue

            dfs(i[0], value + i[1])


    visited = []
    dfs(1,0,True)
    
    visited = []
    dfs(ans.index(max(ans)),0,True)
    
        #dfs(i, 0, True)
    print(max(ans))


main()
