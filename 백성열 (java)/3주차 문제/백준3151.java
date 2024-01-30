import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int[] list;
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        list = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            list[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(list);
        long ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int target = -1 * (list[i] + list[j]);

                int start = j + 1;
                int end = n;
                while (start < end) {
                    int mid = (start + end) / 2;
                    if (list[mid] >= target) {
                        end = mid;
                    } else {
                        start = mid + 1;
                    }
                }
                int lowRound = start;

                start = j + 1;
                end = n;
                while (start < end) {
                    int mid = (start + end) / 2;
                    if (list[mid] > target) {
                        end = mid;
                    } else {
                        start = mid + 1;
                    }
                }
                int upRound = start;
                ans += (upRound - lowRound);
            }
        }

        System.out.println(ans);
    }
}