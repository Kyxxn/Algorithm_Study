import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
  N = int(input())
  jiwon = [list(map(int, input().split())) for _ in range(N)]
  jiwon_sort = sorted(jiwon)  # 지원자를 정렬함으로써 서류심사 성적을 비교대상에서 제외한다. 
  cnt = 1
  top = 0
  for k in range(1, len(jiwon_sort)):
    if jiwon_sort[k][1] < jiwon_sort[top][1]:  # i번째 사람의 면접 성적이 0~(i~1)번째 사람들의 모든 면접 성적보다 순위가 높으면 채용
      top = k
      cnt += 1