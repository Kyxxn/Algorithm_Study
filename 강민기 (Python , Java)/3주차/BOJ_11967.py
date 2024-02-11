


#불켜기


from sys import stdin
from collections import deque


input = stdin.readline



N , M = map(int , input().split(" "))

fire_map = [[0 for __ in range(N+1)] for _ in range(N+1)] # 불 켜진 여부

visit = [[0 for __ in range(N+1)] for _ in range(N+1)] # 방문 여부
direc = [[1,0],[-1,0],[0,1],[0,-1]] 



#초기 세팅

q = deque() # 큐
fire_map[1][1] = 1
q.append((1,1))
visit[1][1] = 1

dic = {} # 불 킬 수 있는 방 목록

for i in range(N+1):
    for j in range(N+1):
         dic[(i,j)] = []


for _ in range(M):
    x,y,a,b = map(int , input().split(" "))
    dic[(x,y)].append((a,b))


count = 1
while q:
    cur = q.popleft()
    if dic[cur]: # 현재 방에서 킬 수 있는 방의 불을 킴
        for i in dic[cur]:
            if fire_map[i[0]][i[1]] == 0:
                fire_map[i[0]][i[1]] = 1
                count +=1
                for d in direc: # 불이 켜지는 방이 방문 가능했던 방이었을때
                    next_x = i[0] + d[0]
                    next_y = i[1] + d[1]
                    if 1<= next_x <= N and 1<= next_y <= N:
                        if visit[next_x][next_y] == 1 and fire_map[next_x][next_y] ==1:
                            visit[next_x][next_y] = 1
                            q.append((next_x,next_y))

    for d in direc: # 현재 방에서 이동 가능한 방을 이동 
        next_x = cur[0] + d[0]
        next_y = cur[1] + d[1]
        if 1<= next_x <= N and 1<= next_y <= N:
            if visit[next_x][next_y] == 0 and fire_map[next_x][next_y] ==1:
                visit[next_x][next_y] = 1
                q.append((next_x,next_y))
                
print(count)

