import java.util.*;

public class 상담원인원 {
    public int solution(int k, int n, int[][] reqs) {
        // 각 상담 유형별 요청 목록 초기화
        ArrayList<Point>[] requestList = new ArrayList[k];
        for (int i = 0; i < k; i++) {
            requestList[i] = new ArrayList<>();
        }
        for (int[] req : reqs) {
            int type = req[2] - 1; // 상담 유형 인덱스
            requestList[type].add(new Point(req[0], req[1]));
        }

        // 각 유형에 대해 멘토 수에 따른 총 대기 시간 계산
        int[][] waitingTime = new int[k][n - k + 2];
        for (int i = 0; i < k; i++) {
            for (int j = 1; j <= n - k + 1; j++) {
                waitingTime[i][j] = calWaitingTime(requestList[i], j);
            }
        }
        // 최소 총 대기 시간 계산
        int result = calTotalWaitingTime(k, n, waitingTime);
        return result;
    }

    public int calTotalWaitingTime(int k, int n, int[][] waitingTime) {
        int remainingMentors = n - k;
        int[] mentorCount = new int[k];
        Arrays.fill(mentorCount, 1);
        while (remainingMentors-- > 0) {
            int maxDiff = 0;
            int maxIndex = 0;
            for (int i = 0; i < k; i++) {
                if (mentorCount[i] == n - k + 1) continue;
                int diff = waitingTime[i][mentorCount[i]] - waitingTime[i][mentorCount[i] + 1];
                if (diff > maxDiff) {
                    maxDiff = diff;
                    maxIndex = i;
                }
            }
            mentorCount[maxIndex]++;
        }

        // 최종 총 대기 시간 계산
        int total = 0;
        for (int i = 0; i < k; i++) {
            total += waitingTime[i][mentorCount[i]];
        }
        return total;
    }

    public int calWaitingTime(List<Point> requestList, int mentorCount) {
        int totalWaitingTime = 0;
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        for (int i = 0; i < mentorCount; i++) queue.add(0);

        for (Point request : requestList) {
            int earliestEndTime = queue.poll();
            if (earliestEndTime <= request.startTime) {
                queue.add(request.startTime + request.duration);
            } else {
                totalWaitingTime += earliestEndTime - request.startTime;
                queue.add(earliestEndTime + request.duration);
            }
        }
        return totalWaitingTime;
    }
    class Point {
        int startTime, duration;

        public Point(int startTime, int duration) {
            this.startTime = startTime;
            this.duration = duration;
        }
    }

}
