import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    people = []
    n = int(input())

    for _ in range(n):
        people.append(tuple(map(int, input().split())))

    people.sort(key=lambda x: x[0])

    count = 1
    min_rank = people[0][1]

    for i in range(1, n):
        if people[i][1] < min_rank:
            count += 1
            min_rank = people[i][1]

    print(count)
