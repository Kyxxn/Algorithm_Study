# 흙길 보수하기


from sys import stdin
input = stdin.readline



n, L = map(int, input().split())
pool = [tuple(map(int, input().split())) for _ in range(n)]


# 웅덩이의 첫 시작 주소를 기준으로 오름 차순 정렬
pool.sort(key=lambda x:x[0])

# 덮여져 있는 마지막 널빤지의 위치 
cur = 0
# 널빤지의 개수 
count = 0


for start, end in pool:

    # 이전 웅덩이에서 덮은 널빤지가 해당 웅덩이를 덮고있는 경우 
    if cur > start:
        start = cur
    # 널빤지의 개수 카운트 
    while start < end:
        start += L # 길이 만큼 더하기
        count += 1 # 갯수 갱신
    cur = start

print(count)