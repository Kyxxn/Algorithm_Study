#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, k;
    cin >> n >> k;

    const int INF = INT_MAX;
    vector<vector<int>> graph(n + 1, vector<int>(n + 1, INF));

    for (int i = 1; i <= n; ++i)
        graph[i][i] = 0;

    for (int i = 0; i < k; ++i) {
        int u, v;
        cin >> u >> v;
        graph[u][v] = 1;
        graph[v][u] = -1;
    }

    // 플로이드-워셜(Floyd Warshall) 알고리즘
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            for (int k = 1; k <= n; ++k) {
                if (graph[j][i] == -1 && graph[i][k] == -1)
                    graph[j][k] = -1;
                else if (graph[j][i] == 1 && graph[i][k] == 1)
                    graph[j][k] = 1;
            }
        }
    }

    int s;
    cin >> s;
    for (int i = 0; i < s; ++i) {
        int u, v;
        cin >> u >> v;

        if (graph[u][v] == INF)
            cout << "0\n";
        else if (graph[u][v] >= 0)
            cout << "-1\n";
        else
            cout << "1\n";
    }

    return 0;
}
