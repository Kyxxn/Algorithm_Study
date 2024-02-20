"""
처음에 이중 for문을 이용해서 풀었지만, 시간초과로 인해 실패
stack을 이용하여 이전의 수를 저장했다가, 큰 수가 나오면 다시 갱신
"""

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i, num in enumerate(numbers):
      # 스택에 들어있는 것은 index, 아직 큰수를 찾지 못한 수로 생각하면 됨
        while(stack and numbers[stack[-1]] < num):  # 스택의 제일 위에 있는 index의 수가 현재 숫자보다 작을때
            a = stack.pop() 
            answer[a] = num
        stack.append(i)
    return answer