import java.io.*;
import java.util.*;

public class 백준1613 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] temp = br.readLine().split(" ");
        int N = Integer.parseInt(temp[0]);
        int event = Integer.parseInt(temp[1]);

        boolean[][] eventOrder = new boolean[N + 1][N + 1];

        for (int i = 0; i < event; i++) {
            temp = br.readLine().split(" ");
            int earlierEvent = Integer.parseInt(temp[0]);
            int laterEvent = Integer.parseInt(temp[1]);
            eventOrder[earlierEvent][laterEvent] = true;
        }

        // 플로이드–워셜 알고리즘
        for (int k = 1; k <= N; k++) {
            for (int i = 1; i <= N; i++) {
                for (int j = 1; j <= N; j++) {
                    if (eventOrder[i][k] && eventOrder[k][j]) {
                        eventOrder[i][j] = true;
                    }
                }
            }
        }

        int result = Integer.parseInt(br.readLine());

        for (int i = 0; i < result; i++) {
            temp = br.readLine().split(" ");
            int a = Integer.parseInt(temp[0]);
            int b = Integer.parseInt(temp[1]);

            if (eventOrder[a][b])
                System.out.println(-1);
            else if (eventOrder[b][a])
                System.out.println(1);
            else
                System.out.println(0);
        }

        br.close();
    }
}
// dfs(실패)
    /*static ArrayList<Integer>[] graph;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new tempStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        graph = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        dp = new int[n + 1][n + 1];

        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
        }

        int s = Integer.parseInt(br.readLine());
        for (int i = 0; i < s; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (dp[a][b] == 0) {
                if (dfs(a, b, n)) {
                    dp[a][b] = -1;
                    dp[b][a] = 1;
                }
            }

            System.out.println(dp[a][b]);
        }
    }

    static boolean dfs(int current, int target, int n) {
        if (current == target) return true;

        for (int next : graph[current]) {
            if (dp[current][next] != 0) { // 이미 계산된 경로 확인
                if (dp[current][next] == -1 && dfs(next, target, n)) {
                    return true;
                }
            } else {
                if (dfs(next, target, n)) {
                    dp[current][next] = -1;
                    dp[next][current] = 1;
                    return true;
                }
            }
        }
        return false;
    }*/
