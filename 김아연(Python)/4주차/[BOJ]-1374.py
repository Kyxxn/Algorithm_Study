# 강의 시작 시간을 기준으로 오름차순 정렬한 뒤, 이를 하나씩 탐색한다.
# 강의 끝나는 시간을 기준으로 큐을 구성해 시작 시간보다 일찍 끝나는 강의는 모두 뺀다.
# 매번 강의를 탐색할 때마다 최소힙의 개수를 구해 이의 최대값을 구한 뒤, 이를 출력한다. (이 부분이 생각해내기 어려웠다.)

# 처음 풀이, 시간이 오래걸림, pypy3으로 제출
import sys
input = sys.stdin.readline

N = int(input())

lacture = []
room = []

for _ in range(N):
  num, start, end = map(int,input().split())
  lacture.append([num, start, end])

lacture = sorted(lacture, key = lambda x: x[0])
lacture = sorted(lacture, key = lambda x: x[1])

cnt = 0

for n,s,e in lacture:
  room.append(e)
  if len(room) > 0:
    for i in room:
      if i <= s:
        room.pop(room.index(i))
  cnt = max(cnt, len(room)) # 중요 

print(cnt)


# 다른사람 풀이를 참고한 풀이(시간이 훨신 줄어듦)
import sys
import heapq  # 새로알게된 것, 최댓값과 최솟값을 찾는 연산을 빠르게 하기위한 것
input = sys.stdin.readline

N = int(input())

lacture = []
room = []

for _ in range(N):
  num, start, end = map(int,input().split())
  lacture.append([num, start, end])

lacture = sorted(lacture, key = lambda x: x[0])
lacture = sorted(lacture, key = lambda x: x[1])

cnt = 0

for n,s,e in lacture:
  while(room and room[0] <= s):
    heapq.heappop(room)  # 현재 진행 중인 강의에서 종료시간이 가장 빠른것을 찾아서 뺀다. 
  heapq.heappush(room,e) # 종료시간 삽입
  cnt = max(cnt, len(room)) # 강의실 수 갱신

print(cnt)