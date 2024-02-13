const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "ex.txt";
const input = fs.readFileSync(filePath, "utf8").trim().split("\n");

const N = Number(input[0]);

const arr = [];
for (let i = 1; i <= N; i++) {
  const [num, start, end] = input[i].split(" ").map(Number);

  arr.push([start, 1]); // 사용중인 강의실 + 1
  arr.push([end, -1]); // 사용중인 강의실 - 1
}

arr.sort((a, b) => {
  // 시간이 같으면
  if (a[0] === b[0]) {
    // 종료시간부터 정렬
    return a[1] - b[1];
  }

  // 시작, 종료 관계없이 시간을 오름차순으로 정렬
  return a[0] - b[0];
});

let cnt = 0;
let result = 0;
arr.forEach((time) => {
  cnt += time[1]; // 시작시간일 경우 강의실 +1, 종료시간일 경우 강의실 -1
  result = Math.max(cnt, result); // 매 시간마다 사용중인 강의실의 최대 갯수 설정
});

console.log(result);
