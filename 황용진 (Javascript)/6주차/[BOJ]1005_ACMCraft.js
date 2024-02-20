const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "ex.txt";
const input = fs.readFileSync(filePath, "utf8").trim().split("\n");

const T = Number(input[0]);
const answer = [];
let line = 1;

for (let i = 0; i < T; i++) {
  answer.push(solution(line));
}

console.log(answer.join("\n"));

function solution(L) {
  const [N, K] = input[L].split(" ").map(Number);
  line += K + 3;

  const target = Number(input[line - 1]);

  const build = input[L + 1].split(" ").map(Number);
  build.unshift(-1);

  const acc = [...build];

  const prev_cnt = new Array(N + 1).fill(0);
  const graph = Array.from({ length: N + 1 }, () => []);

  input.slice(L + 2, L + 2 + K).forEach((eL) => {
    const [prev, next] = eL.split(" ").map(Number);

    graph[prev].push(next);
    prev_cnt[next]++;
  });

  const q = [];

  for (let i = 1; i <= N; i++) {
    if (prev_cnt[i] === 0) q.push(i);
  }

  while (q.length) {
    const curr = q.shift();

    for (let i = 0; i < graph[curr].length; i++) {
      const next = graph[curr][i];

      if (acc[next] < acc[curr] + build[next]) {
        acc[next] = acc[curr] + build[next];
      }

      prev_cnt[next]--;

      if (prev_cnt[next] === 0) q.push(next);
    }
  }

  return acc[target];
}
