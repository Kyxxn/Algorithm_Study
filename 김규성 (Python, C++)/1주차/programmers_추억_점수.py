
def solution(name, yearning, photo):
    answer = []
    person_list = {}

    for i in range(len(name)):
        person_list[name[i]] = yearning[i]

    for i in range(len(photo)):
        yearning_point = 0

        for j in range(len(photo[i])):
            if person_list.get(photo[i][j]):
                yearning_point += person_list[photo[i][j]]
            else:
                continue

        answer.append(yearning_point)

    return answer