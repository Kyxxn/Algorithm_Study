import java.util.*;

class Solution {
    int[] dx = {1,0,0,-1};
    int[] dy = {0,-1,1,0};
    String[] dir = {"d","l","r","u"};
    int endX;
    int endY;
    int n,m;
    boolean[][][] visited = new boolean[51][51][2501];
    boolean finish = false;
    List<Integer> result;
    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        String answer = "";
        this.n = n;
        this.m = m;
        endX = r;
        endY = c;
        dfs(x,y,k,new ArrayList<>());
        StringBuilder sb = new StringBuilder();
        if(result == null) answer = "impossible";
        else {
            for(int i : result){
                sb.append(dir[i]);
            }
            answer = sb.toString();
        }
        return answer;
    }

    void dfs(int x, int y, int k, List<Integer> cnt){
        if(finish) return;
        if(k <= 0){
            if(x == endX && y == endY) {
                result = cnt;
                finish = true;
            }
            return;
        }

        for(int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx > n || ny > m || nx < 1 || ny < 1 || visited[nx][ny][k-1]) continue;
            visited[nx][ny][k-1] = true;
            List<Integer> list = new ArrayList<Integer>(cnt);
            list.add(i);
            dfs(nx,ny,k-1,list);
            if(finish) return;
        }
    }
}