"""
백트래킹 알고리즘을 사용하여 알파벳이 증가하는 순서로 암호를 생성해 준다.
암호문의 길이가 L이 되면 자음과 모음 개수를 확인해 준다.
조건이 맞으면 암호문을 출력해 준다.
"""

import sys
input = sys.stdin.readline

L, C = map(int, input().split())  # 암호의 길이와 입력받는 알파벳 갯수 입력
words = list(input().split())  # 알파벳입력
arr = []  # 암호가 들어갈 배열
words.sort()  # 알파벳순으로 정렬


def func(start): 
  # 종료조건
  if(len(arr) == L):  # 암호가 들어간 배열의 길이가 L일때
    a,b = 0,0  # 자음과 모음 수 초기화
    for i in arr:  # 암호가 들어간 배열순회
      if i in 'aeiou':  # 모음 확인
        a += 1  # 모음이 있으면 모음의 갯수 증가
      else:  # 자음이 있으면
        b += 1  # 자음 갯수 증가
    if a >= 1 and b >= 2:  # 모음이 최소 1개이상, 자음이 최소 2개이상이면
      print(''.join(arr))  # 암호 출력
    return 

  for i in range(start, C):
    if words[i] not in arr:  # 알파벳이 arr안에 없으면
      arr.append(words[i])   # 추가
      func(i+1)  # 시작인덱스를 증가 시킨 후 함수 호출
      arr.pop()  # arr에 있는 알파벳 제거

func(0)