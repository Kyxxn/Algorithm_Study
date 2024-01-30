import java.util.Scanner;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        int cnt = 0;
        ArrayList<temp>[][] arr = new ArrayList[N+1][N+1];
        Queue<temp> q = new LinkedList<>();
        int[][] visited = new int[N+1][N+1];
        int[][] light = new int[N+1][N+1];
        int[] X = {1, -1, 0, 0};
        int[] Y = {0, 0, 1, -1};

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                arr[i][j] = new ArrayList<>();
            }
        }

        for (int i = 0; i < M; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            int a = sc.nextInt();
            int b = sc.nextInt();
            arr[x][y].add(new temp(a, b));
        }

        q.add(new temp(1, 1));
        light[1][1] = 1;
        cnt++;

        int[][] move = new int[N+1][N+1];

        while (!q.isEmpty()) {
            temp now = q.poll();
            visited[now.x][now.y] = 1;

            for (temp r : arr[now.x][now.y]) {
                if (light[r.x][r.y] == 1) continue;

                light[r.x][r.y] = 1;
                cnt++;
                if (move[r.x][r.y] == 1) q.add(new temp(r.x, r.y));
            }

            for (int i = 0; i < 4; i++) {
                int nextX = now.x + X[i];
                int nextY = now.y + Y[i];

                if (nextX < 1 || nextX > N || nextY < 1 || nextY > N) continue;

                move[nextX][nextY] = 1;

                if (visited[nextX][nextY] == 1 || light[nextX][nextY] == 0) continue;

                q.add(new temp(nextX, nextY));
            }
        }

        System.out.println(cnt);
    }

    static class temp {
        int x, y;

        temp(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
