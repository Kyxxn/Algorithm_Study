def eratos_and_palindrome(N):
    def check_palindrome(M):
        return M == M[::-1]

    # 소수 확인 배열
    arr = [True] * int(1100000+1)
    arr[0] = arr[1] = False

    for i in range(2, int(1100000**0.5)+1):
        if arr[i]:
            for j in range(i+i, 1100000+1, i):
                arr[j] = False

    for i in range(N, 1100000):
        if arr[i]:
            # 팰린드롬 확인 배열
            check_palindrome_arr = [int(digit) for digit in str(i)]

            if check_palindrome(check_palindrome_arr):
                print(i)
                return


n = int(input())
eratos_and_palindrome(n)