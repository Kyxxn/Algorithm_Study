const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "ex.txt";
const input = fs.readFileSync(filePath, "utf8").trim().split("\n");

const n = Number(input[0]);

const stars = Array.from({ length: n }, () => null);
const edges = [];
const ufa = new Array(n + 1);

for (let i = 1; i <= n; i++) {
  let [x, y] = input[i].split(" ").map((e) => parseFloat(e));
  stars[i - 1] = [x, y];
}

for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (i === j) continue;

    let dist =
      ((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2) **
      0.5;
    edges.push([dist, i, j]);
  }
}

for (let i = 1; i <= n; i++) {
  ufa[i] = i;
}

function find(num) {
  if (ufa[num] === num) return num;
  else {
    ufa[num] = find(ufa[num]);
    return ufa[num];
  }
}

function union(x, y) {
  let X = find(x);
  let Y = find(y);
  if (X !== Y) ufa[X] = Y;
}

edges.sort((a, b) => a[0] - b[0]);
function solution() {
  let sum = 0;
  let cnt = 0;

  for (const [dist, i, j] of edges) {
    if (find(i) === find(j)) continue;

    sum += dist;
    union(i, j);
    cnt++;

    if (cnt === n - 1) break;
  }

  console.log(sum);
  console.log(edges);
}

solution();
