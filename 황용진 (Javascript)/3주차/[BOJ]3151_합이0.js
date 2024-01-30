const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "ex.txt";
const input = fs.readFileSync(filePath, "utf8").trim().split("\n");

const N = Number(input[0]);
const arr = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

function solution() {
  let cnt = 0;

  for (let i = 0; i < N - 2; i++) {
    if (arr[i] > 0) break;
    let left = i + 1;
    let right = N - 1;

    while (left < right) {
      let sum = arr[i] + arr[left] + arr[right];
      if (sum === 0) {
        if (arr[left] === arr[right]) {
          let n = right - left + 1;
          cnt += Math.floor((n * (n - 1)) / 2);
          break;
        }
        let lCnt = 1;
        let rCnt = 1;
        while (left + 1 < right && arr[left] === arr[left + 1]) {
          left++;
          lCnt++;
        }
        while (left < right - 1 && arr[right - 1] === arr[right]) {
          right--;
          rCnt++;
        }
        cnt += lCnt * rCnt;
      }
      if (sum > 0) {
        right--;
      } else {
        left++;
      }
    }
  }
  return cnt;
}

console.log(solution());
