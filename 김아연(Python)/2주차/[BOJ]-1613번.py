# 내 풀이
import sys
input = sys.stdin.readline

n, k = map(int,input().split())

floyd = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(k):
  a, b = map(int,input().split())
  floyd[a][b] = 1

for i in range(1,n+1):  # 시작
  for j in range(1, n+1):  # 중간
    for k in range(1, n+1):  # 끝
      if floyd[j][i] + floyd[i][k] == 2:  # 중간을 거쳐서 가는 경로가 있으면
        floyd[j][k] = 1 

s = int(input())
want = []
for _ in range(s):
  c,d = map(int,input().split())
  if floyd[c][d] == 1:  # 앞에 있는 사건이 먼저 일어났다면
    print(-1)
  elif floyd[d][c] == 1:  # 뒤에 있는 사건이 먼저 있어났다면
    print(1)
  else:
    print(0)