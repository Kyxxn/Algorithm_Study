function solution(k, tangerine) {
  const weight = {};

  tangerine.forEach((n) => {
    weight[n] = ++weight[n] || 1;
  });

  const kind = Object.values(weight).sort((a, b) => b - a);

  let sum = 0;
  let answer = 0;

  for (let num of kind) {
    answer++;
    sum += num;

    if (sum >= k) break;
  }
  return answer;
}
