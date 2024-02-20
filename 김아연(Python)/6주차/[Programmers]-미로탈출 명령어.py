"""
백트래킹으로 풀려고 했지만 시간 초과로 인해 다른 사람 풀이를 참고하여 풂
그리디하게 푼 풀이
dlru순으로 명령어를 사용해야하기 때문에 앞서서 d를 최대한 사용하고, 그 다음 l을 많이 사용한다.
이후 ru를 반복해서 사용하면 된다.
1. 위 로직으로 매번 이동거리 계산 후 경로 추가
2. 현재 좌표에서 도착 좌표까지 거리와 이동할 거리가 남았다면, 위 반복

* 시작 좌표부터 도착 좌표까지의 거리와 k가 모두 동일한 홀수나, 짝수여야 이동 좌표로 도착 가능
"""

def remain(x, y, r, c): # 남은거리 계산 함수
    return abs(x-r) + abs(y-c)

def solution(n, m, x, y, r, c, k):
    if (k - remain(x, y, r, c)) % 2 or remain(x, y, r, c) > k:
        return "impossible"
    
    answer = ''
    move = 0

    # 아래로 최대한 이동
    while x < n and (k - move) > remain(x, y, r, c):
        move += 1
        x += 1
        answer += 'd'

    # 좌로 최대한 이동
    while 1 < y and (k - move) > remain(x, y, r, c):
        move += 1
        y -= 1
        answer += 'l'

    # 우좌로 반복 이동
    while (k - move) > remain(x, y, r, c):
        move += 2
        answer += 'rl'

    # 가야할 길로 dlru 순으로 이동 
    if x < r:
        answer += 'd' * (r-x)
        x = r
    if y > c:
        answer += 'l' * (y-c)
        y = c
    if y < c:
        answer += 'r' * (c-y)
        y = c
    if x > r:
        answer += 'u' * (x-r)
        x = r

    return answer