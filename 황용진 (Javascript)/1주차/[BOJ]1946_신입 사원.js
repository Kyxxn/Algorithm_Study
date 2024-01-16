const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "ex.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const T = Number(input[0]);

function solution(n, arr) {
  let cnt = 1;
  let min = n;
  for (let i = 2; i < arr.length; i++) {
    if (arr[i] < min) {
      cnt++;
      min = arr[i];
    }
  }
  return cnt;
}

let row = 1;
for (let i = 0; i < T; i++) {
  const N = Number(input[row++]);
  const arr = new Array(N + 1).fill(Infinity);
  for (let j = 0; j < N; j++) {
    const [n, m] = input[row++].split(" ").map(Number);
    arr[n] = m;
  }

  console.log(solution(arr[1], arr));
}
