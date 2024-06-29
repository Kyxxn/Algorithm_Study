import java.io.*;
import java.util.*;

public class Main {
   
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        App[] apps = new App[n];

        StringTokenizer st1 = new StringTokenizer(br.readLine());
        StringTokenizer st2 = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            int memory = Integer.parseInt(st1.nextToken());
            int price = Integer.parseInt(st2.nextToken());
            apps[i] = new App(memory, price);
        }

        int[] memoryArr = new int[10001];
        for (int i = 0; i < n; i++) {
            int mi = apps[i].memory;
            int pi = apps[i].price;
            for (int j = 10000; j >= pi; j--) {
                if (memoryArr[j] < memoryArr[j - pi] + mi) {
                    memoryArr[j] = memoryArr[j - pi] + mi;
                }
            }
        }

        int price = 0;
        while (memoryArr[price] < m) {
            price++;
        }

        bw.write(price + "");
        bw.close();
    }
    static class App {
        int memory, price;

        App(int memory, int price) {
            this.memory = memory;
            this.price = price;
        }
    }
}