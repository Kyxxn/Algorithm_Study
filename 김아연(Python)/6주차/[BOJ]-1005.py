"""
BFS는 시간초과
위상 정렬을 이용하여 푼 문제 (cycel이 없고 directed 일 때 풀 때 사용하는 알고리즘으로 queue에 탐색할 원소를 넣을 때의 조건은 'indgree가 0일 경우" 이다.)
1. 위상 정렬의 첫 시작은 아무것도 건들지 않은 상태에서 진입차수가 0인 것부터 시작(진입차수: 들어오는 간선)
2. 하나씩 탐색하면서 해당 노드까지 가는 최장거리를 갱신한다(DP). 
  - 이 때 해당 노드의 진입차수가 아직 남아있더라도 max연산을 통해 모든 경우에서 최댓값을 구해준다.
3. 이 과정에서 진입차수가 0이 된다면 큐에 넣어서 다음 탐색을 위한 발판으로 한다.
"""

import sys
from collections import deque
sys.setrecursionlimit(10000) # 재귀 깊이 설정
input = sys.stdin.readline

def topology_sort(): # 위상정렬 함수
  result = [0] * (N+1)  # 걸리는 시간
  q = deque()

  # 진입차수가 0인것부터 시작
  for i in range(1, N+1):
    if indgree[i] == 0:  # 위상이 0인 건물을 큐에 넣고, result에 time 갱신
      q.append(i)
      result[i] = time[i]

  while q:
    now = q.popleft()

    for next in build[now]:
      result[next] = max(time[next] + result[now], result[next]) # 건물을 동시에 짓기 때문에 최댓값을 result에 갱신
      indgree[next] -= 1 # 진입 간선을 하나 빼준다(건물을 지었으므로)
      if indgree[next] == 0: # 건물을 바로 지을 수 있는 조건이면, 큐에 넣어준다.
        q.append(next)
        
  return result[W]

T = int(input())

for _ in range(T):
  N, K = map(int, input().split())  # 건물의 수, 간선의 갯수
  time = [0] + list(map(int,input().split()))  # 건물을 짓는데 걸리는 시간
  indgree = [0] * (N+1) # 진입간선의 수
  build = [[] for _ in range(N+1)] # 간선
  for _ in range(K):
    X, Y = map(int,input().split())
    build[X].append(Y) # 간선 추가
    indgree[Y] += 1 # 진입간선 증가
  W = int(input()) # 목표
  print(topology_sort())