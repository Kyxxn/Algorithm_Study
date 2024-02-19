def solution(n, m, x, y, r, c, k):
    
    answer = ''
    
    if (abs(x-r) + abs(y-c)) > k or (abs(x-r) + abs(y-c)) % 2 != k % 2:
        return "impossible"
    
    alpa = ['d', 'l', 'r', 'u']
    
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    

    posX = x
    posY = y

    move = 0

    while (True):
        if posX == r and posY == c and move == k:
            break
        for i in range(4):
            if 0 < posX + dx[i] <= n and 0 < posY + dy[i] <= m:
                if abs(posX + dx[i] - r) + abs(posY + dy[i] - c) <= k - move:
                    print(alpa[i])
                    answer += alpa[i]
                    posX += dx[i]
                    posY += dy[i]
                    move += 1
                    break

    return answer

## d 아래 ㅣ 왼  r 오른 u 위

n, m, x, y, r, c, k = [3,3,1,2,3,3,4]
n, m, x, y, r, c, k = [3,4,2,3,3,1,5]
#n, m, x, y, r, c, k = [6, 6, 2, 6, 6, 5, 11]
#n, m, x, y, r, c, k = [3, 3, 1, 1, 3, 3, 8]


print(solution(n, m, x, y, r, c, k))
