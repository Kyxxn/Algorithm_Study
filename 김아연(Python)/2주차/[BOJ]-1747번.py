# 내 풀이
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def sosu(n):  # 소수 판별 함수
  for i in range(2, int(n**0.5)+1):
    if n%i == 0:
      return False
  return True
    
N = int(input())
result = 0

for num in range(N, 1000001):
  if num == 1:  # num이 1이라면 예외처리
    continue
  if str(num) == str(num)[::-1]:  # 팰린드롬 수라면
    if sosu(num) == True:  # 소수라면
      result = num 
      break

if result == 0:  # 1,000,000일 때
  result = 1003001

print(result)