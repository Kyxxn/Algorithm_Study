import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }

        if (n == 1 || (n == 2 && arr[0] != arr[1])) {
            System.out.print("A");
        } else if (n == 2) {
            System.out.print(arr[0]);
        } else {
            int a, b;
            if (arr[1] == arr[0]) {
                a = 1;
                b = 0;
            } else {
                a = (arr[2] - arr[1]) / (arr[1] - arr[0]);
                b = arr[1] - (arr[0] * a);
            }

            // validate
            int i = 1;
            for (; i < n; i++) {
                if (arr[i] != (arr[i - 1] * a + b))
                    break;
            }
            if (i != n) {
                System.out.print("B");
            } else {
                System.out.print((arr[n - 1] * a + b));
            }
        }
    }
}