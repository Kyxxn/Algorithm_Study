import sys
from collections import defaultdict

input = sys.stdin.readline


def main():
    n = int(input().strip())

    tree = defaultdict(list)

    for _ in range(n - 1):
        n, m, v = map(int, input().split())
        tree[n].append([m, v])
        tree[m].append([n, v])

    leafs = [leaf[0] for leaf in tree.items() if len(leaf[1]) == 1]
    discovered = []

    def dfs(V, value, check=False):
        nonlocal visited  # 방문한 노드
        nonlocal leafs
        nonlocal ans
        if (not check) and V in leafs:
            ans = max(value, ans)
        visited.append(V)

        for i in tree[V]:
            if i[0] in visited:
                continue

            dfs(i[0], value + i[1])

    ans = 0
    for i in leafs:
        visited = []
        dfs(i, 0, True)
    print(ans)


main()
