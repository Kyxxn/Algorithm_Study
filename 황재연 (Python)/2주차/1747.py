import sys
input = sys.stdin.readline



def main():
    num = int(input().strip())
    
    max_num = 1003002

    board = [False,False]+[True] * max_num

    def find_decimal():
        nonlocal board
        for i in range(2,max_num):
            if not board[i]:
                continue
            for j in range(i+i,max_num,i):
                if not board[j]:
                    continue
                board[j] = False
    find_decimal()

    def fine_palindrome(V):
        v = str(V)
        v = list(v)
        lens = len(v)
        return True if v[::-1] == v else False


    for i in range(num,max_num):
        if not board[i]:
            continue
        if fine_palindrome(i):
            print(i)
            break        
    

main()