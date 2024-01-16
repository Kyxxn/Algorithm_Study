import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(1,N):
  a,b,c = map(int, input().split())  # a-부모노드 , b-자식노드, c-가중치
  graph[a].append([b,c])
  graph[b].append([a,c])

distance = [-1] * (N+1)
distance[1] = 0

def dfs(v, d):
  for i in range(len(graph[v])):
    next, nextdis = graph[v][i]
    if distance[next] == -1:
      distance[next] = nextdis + d
      dfs(next, distance[next])

dfs(1,0)
max_idx = distance.index(max(distance)) # 1번에서 가장 먼 노드의 인덱스

distance = [-1] * (N+1)  # 거리 초기화
distance[max_idx] = 0  # 가장 먼 인덱스부터 다시 시작 
dfs(max_idx, 0) 

print(max(distance))