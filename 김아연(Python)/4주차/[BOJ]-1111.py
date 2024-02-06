"""
- N이 1이라면 무조건 A출력
- N이 2라면 
  - x0과 x1이 같으면 제일 처음 수 출력
  - 같지않으면 A출력
- N이 3이상이라면
 - 만약 x1-x0이 0이 아니라면 
   => a는 (x2-x1)/(x0-x1)
 - 0이라면 
   => a는 0
 - b는 x1-x0*a
 - 순차적으로 숫자들이 ax0 + b로 구성되어있는지 확인
   - 맞으면 마지막 숫자에 a,b 대입
   - 틀리면 B출력
"""

import sys
input = sys.stdin.readline

N = int(input())

nums = list(map(int,input().split()))

if N == 1:
  print("A")
if N == 2:
  if nums[0] == nums[1]:
    print(nums[0])
  else:
    print("A")

if N >= 3:
  if (nums[1] - nums[0]) != 0:
    a = (nums[2] - nums[1]) // (nums[1] - nums[0])
  else:
    a = 0
    
  b = nums[1] - nums[0]*a
    
  for i in range(2, len(nums)):
    if nums[i] == nums[i-1]*a+b:
      answer = nums[-1] * a + b
    else:
      answer = "B"
      break  # 이자리에 바로 exit()를 사용해도 무방

  print(answer)