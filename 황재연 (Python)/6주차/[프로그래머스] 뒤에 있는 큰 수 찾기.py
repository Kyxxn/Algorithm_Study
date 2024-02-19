def solution(numbers):

    maxNum = 0

    stack = [0]

    answer = []
    
    for i in numbers[::-1]:
        for j in stack[::-1]:
            if  i < j:
                answer.append(j)
                stack.append(i)
                break
            else:
                stack.pop()
        else:
            answer.append(-1)
            stack.append(i)

    return answer[::-1]


numbers = [1, 5, 1, 1, 1, 3, 7]

print(solution(numbers))