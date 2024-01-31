"""
그래프 탐색을 진행하되, 현재 그래프에서 방문할 수 있는지 여부(즉 불이 켜졌는지 여부)를 저장해야 한다.

1. 현재 좌표에서, 우선 켤 수 있는 스위치는 모조리 켠다.
  - 대상 좌표의 불이 켜졌는지에 대한 여부를 업데이트한다. 
  - 만약 방문하였되 들어갈 수 없었던 좌표라면, 그 좌표를 방문 큐에 삽입한다.
2. 현재 좌표에서 상하좌우를 탐색한다.
  - 유효한 좌표이며( -1 < x, y < N ) 방문하지 않았다면 우선 방문 여부를 업데이트한다.
  - 만일 불이 켜진 좌표라면 그 좌표를 방문 큐에 삽입하고, 그렇지 않으면 넘어간다.
3. 그래프에서 불켜진 방의 합을 도출한다.

처음에 그래프만 사용하여 풀이를 했을 때 답은 나왔지만 시간초과로 해결하지 못했다. 
다른사람 풀이를 참고해서 방문여부를 확인하는 그래프가 이용하여 해결하였다. 
리스트에 원소 포함여부를 확인하는 in은 생각보다 시간을 많은 필요로 한다. 
"""

import sys
from collections import defaultdict
input = sys.stdin.readline

N,M = map(int,input().split())
room = [[0 for _ in range(N+1)] for _ in range(N+1)]  # 방의 불을 나타내는 그래프(0:꺼짐, 1:켜짐)
visited = [[False for _ in range(N+1)] for _ in range(N+1)]  # 방 방문 여부를 나타내는 그래프

# 상하좌우
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

switchs = defaultdict(list) # 처음 알게된 함수, 딕셔너리와 비슷하지만 인자로 주어진 객체의 기본값을 딕셔너리의 초기값으로 지정가능

room[1][1] = 1 # 초기 방 불 켜기
visited[1][1] = True  # 방문 표기

for i in range(M):
  x,y,a,b = map(int,input().split())
  switchs[(x, y)].append([a, b])  # 방과 그 방이 조절할 수 있는 방 입력

def bfs(x,y,switchs):
  queue = [[x,y]]
  while(queue):
      a,b = queue.pop(0)
      for k, v in switchs[(a,b)]: # 조절할 수 있는 방 가져오기 
        if not room[k][v]: # 방 불이 꺼져있으면
          room[k][v] = 1  # 켜기
          if visited[k][v]:  # 방문을 했더라도
            queue.append([k,v])  # 탐색할 방에 추가(늦게 켜진 방에 대해 또 탐색을 해야하므로)

      for k in range(4): # 현재 좌표에서 상하좌우 탐색
        nx, ny = a+dx[k], b+dy[k]
        if 0 < nx <= N and 0 < ny <= N and not visited[nx][ny] : # 범위를 넘지 않고 , 방문하지 않았다면
          visited[nx][ny] = True  # 방문표시 
          if room[nx][ny]: # 불이 켜져있더라도 
            queue.append([nx,ny]) # 다시 탐색

bfs(1,1, switchs)
print(sum(map(sum, room)))