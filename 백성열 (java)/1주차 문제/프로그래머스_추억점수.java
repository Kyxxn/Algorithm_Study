import java.util.HashMap;

public class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        HashMap<String,Integer> map = new HashMap<String,Integer>();
        for(int i = 0 ;i< yearning.length;i++){
            map.put(name[i],yearning[i]);
        }
        for(int i = 0;i<photo.length;i++){
            int result = 0;
            for(int j = 0;j<photo[i].length;j++){
                if(map.get(photo[i][j]) != null){
                    result += map.get(photo[i][j]);
                }
            }
            answer[i] = result;
        }
        return answer;
    }
}