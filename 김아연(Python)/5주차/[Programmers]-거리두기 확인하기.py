"""
대기실을 탐색하면서 각각의 원소를 기준으로 상하좌우만 검사
- 원소가 P일때 => 상하좌우로 P가 없어야함
- 원소가 O일때 => 상하좌우로 P가 1개 이하여야함 (O의 주위를 탐색하는 것이 P의 대각선을 탐색하는 역할)
"""

# 내 풀이
def solution(places):
    answer = [1] * 5
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for i in range(5):
        for j in range(5):
            for k in range(5):  
                if places[i][j][k] == 'P': # 원소가 P일때
                    for l in range(4): # 상하좌우 탐색
                        nx = j + dx[l]
                        ny = k + dy[l]
                        if 0<=nx<5 and 0<=ny<5:  # 범위 조절
                            if places[i][nx][ny] == 'P': # 만약 상하좌우에 응시자가 있으면
                                answer[i] = 0 # 배열에 0 저장
                if places[i][j][k] == 'O':  # 원소가 O일때
                    cnt = 0 # 주위 응시자의 수
                    for l in range(4): # 상하좌우 탐색
                        nx = j + dx[l]
                        ny = k + dy[l]
                        if 0<=nx<5 and 0<=ny<5:
                            if places[i][nx][ny] == 'P':  # 주위에 응시자가 있으면
                                cnt += 1 # 응시자 수 추가
                        if cnt >= 2: # 주위에 응시자 수가 2이상이면
                            answer[i] = 0 # 배열에 0 저장
    return answer

    # for i in range(5):
    #     check = [[0 for _ in range(5)] for _ in range(5)]
    #     for j in range(5):
    #         for k in range(5):
    #             if places[i][j][k] == 'P':
    #                 check[j][k] -= 1
    #                 for l in range(4):
    #                     nx = j+dx[l]
    #                     ny = k+dy[l]
    #                     if 0<=nx<5 and 0<=ny<5:
    #                         check[nx][ny] -= 1
    #             if places[i][j][k] == 'X':
    #                 check[j][k] += 10
    #     for x in range(5):
    #         for y in range(5):
    #             if check[x][y] <= -2:
    #                 answer[i] = 0
    #             else:
    #                 answer[i] = 1