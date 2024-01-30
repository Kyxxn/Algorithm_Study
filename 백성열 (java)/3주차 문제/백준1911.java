import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());
        int[][] water = new int[N][2];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(bf.readLine());
            water[i][0] = Integer.parseInt(st.nextToken());
            water[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(water, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] == o2[0])
                    return Integer.compare(o1[1], o2[1]);
                return Integer.compare(o1[0], o2[0]);
            }
        });

        int planksNeeded = 0;
        int cover = 0;

        for (int i = 0; i < N; i++) {
            if (water[i][0] > cover) {
                cover = water[i][0];
            }
            while (water[i][1] > cover) {
                cover += L;
                planksNeeded++;
            }
        }

        System.out.println(planksNeeded);
        bf.close();
    }
}
