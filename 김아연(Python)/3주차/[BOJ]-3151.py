"""
처음에 조합을 이용하여 학생들을 입력 받은 후 3인조가 될 수 있는 경우를 만들어 합이 0이 되면 팀수를 증가시키는 방법을 이용하였지만 메모리초과가 발생하였다. 
그래서 다른사람의 아이디어를 참고하여 풀었다. 
1. 학생들을 입력받고 정렬을 한다. 
2. 학생의 수 만큼 반복을 한다. 
 - 이분탐색 (left = i+1, right = 학생수-1)
 - result : 세 수의 합
 - 0보다 크면 right-1
 - 0보다 작거나 같으면 left + 1
 (중복을 허용하기 때문에 0일 경우 팀 수에 중복되는 길이를 더하기)
3. 팀 수 출력
"""

import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
students = list(map(int,input().split()))  # 학생입력
students = sorted(students) # 정렬

team = 0

for i in range(len(students)):  # 학생들을 훑기
  left = i+1
  right = len(students)-1
  while(left < right):
    result = students[i] + students[left] + students[right]
    if result > 0:
      right -= 1
    else:
      if result == 0:
        if students[left] == students[right]:
          team += (right - left)
        else:
          idx = bisect_left(students, students[right])  # *bisect : team에 더해줄 때, 중복되는 수의 갯수를 쉽게 구해주는 함수
          team += (right - idx+1)
      left += 1

print(team)