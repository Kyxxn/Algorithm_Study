import java.util.*;

class Solution {
    private char[][][] classRoom;
    private boolean[][] visited;
    private static final int[] dx = {-1, 1, 0, 0};
    private static final int[] dy = {0, 0, -1, 1};

    public int[] solution(String[][] places) {
        int[] answer = new int[5];
        classRoom = new char[5][5][5];

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                classRoom[i][j] = places[i][j].toCharArray();
            }
        }

        for (int i = 0; i < 5; i++) {
            visited = new boolean[5][5];
            boolean isSafe = true;
            for (int j = 0; j < 5 && isSafe; j++) {
                for (int k = 0; k < 5 && isSafe; k++) {
                    if (classRoom[i][j][k] == 'P') {
                        isSafe = dfs(i, j, k, 0);
                    }
                }
            }
            answer[i] = isSafe ? 1 : 0;
        }

        return answer;
    }

    private boolean dfs(int room, int x, int y, int depth) {
        if (x < 0 || y < 0 || x >= 5 || y >= 5 || visited[x][y] || depth > 2) return true;
        if (classRoom[room][x][y] == 'X') return true;
        if (classRoom[room][x][y] == 'P' && depth > 0) return false;

        visited[x][y] = true;

        for (int i = 0; i < 4; i++) {
            if (!dfs(room, x + dx[i], y + dy[i], depth + 1)) {
                return false;
            }
        }

        return true;
    }
}
