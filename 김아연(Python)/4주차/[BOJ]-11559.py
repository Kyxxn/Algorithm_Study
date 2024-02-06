"""
필요한 기능을 세가지 함수로 정리
- 상하좌우 동일한 블록 탐색
- 블록 제거
- 블록 떨어트리기(다른사람 풀이 참고)
"""

import sys
input = sys.stdin.readline

field = [list(input().rstrip()) for _ in range(12)]
answer = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 블록을 떨어트리는 함수
def down():
  for i in range(6):
    for j in range(10, -1, -1): # 역순으로 반복문을 돌며 아래로 불록을 내림
        for k in range(11, j, -1):
          if field[j][i] != '.' and field[k][i] == '.':
            field[k][i] = field[j][i]
            field[j][i] = '.'
            
# 상하좌우로 동일한 블록을 탐색하는 함수
def bfs(x,y):
  queue = []
  queue.append((x,y))
  boom.append((x,y))  # 동일한 블럭의 좌표를 저장하는 리스트
  while queue:
    x, y = queue.pop(0)
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < 12 and 0 <= ny < 6 and field[nx][ny] == field[x][y] and visited[nx][ny] == False:
        queue.append((nx, ny))
        boom.append((nx, ny))
        visited[nx][ny] = True

# 동일한 블럭을 제거하는 함수
def puyo(boom):
  for x, y in boom:
    field[x][y] = '.'

while True:
  boom_cnt = 0
  visited = [[False for _ in range(6)] for _ in range(12)]
  for a in range(12):
    for b in range(6):
      if field[a][b] != '.' and visited[a][b] == False :
        visited[a][b] = True
        boom = []
        bfs(a,b)

        if len(boom) >= 4: # 저장된 블록이 4개 이상이면
          boom_cnt = 1
          puyo(boom) # 블록을 터트린다
  if boom_cnt == 0: # 터트릴 블럭이 없다면
    break  # 정지
  down() # 블럭을 터트리고 남은 블럭을 내린다. 
  answer += 1
print(answer)