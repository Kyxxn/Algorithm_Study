import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.PriorityQueue;

public class Main {
    static List<Edges>[] graph;

    public static void prim(int start, int n) {
        boolean[] visited = new boolean[n+1];
        PriorityQueue<Edges> pq = new PriorityQueue<>();
        double total = 0;
        pq.offer(new Edges(start, 0.0));

        while(!pq.isEmpty()) {
            Edges edge = pq.poll();
            if(visited[edge.w]) continue;
            visited[edge.w] = true;
            total += edge.cost;
            for(Edges e : graph[edge.w]) {
                if(!visited[e.w]) {
                    pq.offer(e);
                }
            }
        }
        System.out.printf("%.2f", total);
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        double[][] location = new double[n+1][2];
        graph = new ArrayList[n+1];
        for(int i=1; i<=n; i++) {
            graph[i] = new ArrayList<>();
        }

        for(int i=1; i<=n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            location[i][0] = Double.parseDouble(st.nextToken());
            location[i][1] = Double.parseDouble(st.nextToken());
        }

        for(int i=1; i<n; i++) {
            for(int j=i+1; j<=n; j++) {
                double dis = Math.sqrt(Math.pow(location[i][0]-location[j][0],2) + Math.pow(location[i][1]-location[j][1],2));
                graph[i].add(new Edges(j, dis));
                graph[j].add(new Edges(i, dis));
            }
        }

        prim(1, n);
    }
    
    class Edges implements Comparable<Edges> {
    int w;
    double cost;

    Edges(int w, double cost) {
        this.w = w;
        this.cost = cost;
    }

    @Override
    public int compareTo(Edges o) {
        return Double.compare(this.cost, o.cost);
    }
}
}

