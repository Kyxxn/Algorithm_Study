import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

def topological_sort(graph_dict, indegree):
    queue = deque()
    result = []
    
    for node in graph_dict.keys():
        if indegree[node] == 0:
            queue.append(node)
    
    while queue:
        cur = queue.popleft()
        result.append(cur)
        
        for adj_node in graph_dict[cur]:
            indegree[adj_node] -= 1
            
            if indegree[adj_node] == 0:
                queue.append(adj_node)
    
    return result

def main():
    n, k = map(int, input().split())

    value = [0] + list(map(int, input().split()))
    saves = [0] + [0] * n
    graph_dict = defaultdict(list)
    indegree = [0] * (n + 1)

    for __ in range(k):
        r, c = map(int, input().split())
        graph_dict[r].append(c)
        indegree[c] += 1

    goal = int(input().strip())

    sorted_nodes = topological_sort(graph_dict, indegree)

    for node in sorted_nodes:
        if node == goal:
            break

        for adj_node in graph_dict[node]:
            if value[node] + saves[node] > saves[adj_node]:
                saves[adj_node] = value[node] + saves[node]

    return saves[goal] + value[goal]

if __name__ == '__main__':

    cases = int(input().strip())

    for _ in range(cases):
        print(main())
