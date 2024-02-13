def solution(places):
    answer = []
    for place in places:
        board = [[0] * 5 for _ in range(5)]
        for i , xval in enumerate(place) :
            for j , yval in enumerate(xval):
                if  yval == "X":
                    continue
                elif yval == "O":
                    continue
                else:
                    for x,y in [(i,j),(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                        if x < 0 or x >= 5 or y < 0 or y >= 5:
                            continue
                        if place[x][y] == "X":
                            continue
                        board[x][y] += 1
        
        maxNum = max([j for i in board for j in i ])
        if maxNum > 1:
            answer.append(0)
        else:
            answer.append(1)
    
    return answer


places = [["POOOO", "XPOOO", "OOOOO", "OOOOO", "OOOOO"], ["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print (solution(places))