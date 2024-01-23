import java.util.*;

public class Solution {
    static public int solution(int k, int[] tangerines) {
        int answer = 0;
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int size : tangerines) {
            map.put(size, map.getOrDefault(size, 0) + 1);
        }

        List<Tangerine> ve = new ArrayList<>();
        for (Map.Entry<Integer, Integer> element : map.entrySet()) {
            ve.add(new Tangerine(element.getKey(), element.getValue()));
        }

        Collections.sort(ve, new Comparator<Tangerine>() {
            @Override
            public int compare(Tangerine o1, Tangerine o2) {
                return Integer.compare(o2.num, o1.num);
            }
        });

        int num = 0;
        for (Tangerine temp : ve) {
            if (num < k) {
                num += temp.num;
                answer++;
            } else {
                break;
            }
        }

        return answer;
    }

    static class Tangerine {
        
        int size;
        int num;

        Tangerine(int size, int num) {
            this.size = size;
            this.num = num;
        }
    }
}