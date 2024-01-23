import java.util.Scanner;

public class backjoon1747 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.close();

        while (true) {
            if (Palindrome(N) && Prime(N)) {
                System.out.println(N);
                break;
            }
            N++;
            if (N > 1003001) {
                break;
            }
        }
    }

    // 소수 판별
    public static boolean Prime(int N) {
        if (N < 2) return false;
        for (int i = 2; i * i <= N; i++) {
            if (N % i == 0) return false;
        }
        return true;
    }

    // 펠린드롬 판별
    public static boolean Palindrome(int N) {
        String str = Integer.toString(N);
        int start = 0;
        int end = str.length() - 1;
        while (start <= end) {
            if (str.charAt(start) != str.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
}