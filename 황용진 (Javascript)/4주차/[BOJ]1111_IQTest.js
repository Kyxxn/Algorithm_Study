const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "ex.txt";
const input = fs.readFileSync(filePath, "utf8").trim().split("\n");

const N = Number(input[0]);

const arr = input[1].split(" ").map(Number);

// ax + b
// a = 2, b = 1
// 3
// 3 7 11 B

// 수열의 길이가 1일 경우
if (N === 1) {
  console.log("A");
}

// 수열의 길이가 2일 경우
if (N === 2) {
  // 첫번째 항과 두번째 항이 같음
  if (arr[0] === arr[1]) {
    console.log(arr[1]);
  }
  // 첫번째 항과 두번째 항이 다름
  else {
    console.log("A");
  }
}
// 수열의 길이가 3 이상일 경우
else if (N >= 3) {
  // ax + b
  let a = 0,
    b = 0;
  let flag = true;

  if (arr[1] - arr[0] !== 0) {
    a = (arr[2] - arr[1]) / (arr[1] - arr[0]);
    // a가 정수가 아니면 B
    if (a % 1 !== 0) {
      console.log("B");
      flag = false;
    }
  }

  b = arr[1] - arr[0] * a;

  for (let i = 1; i < N; i++) {
    // 식의 결과가 다르면 B
    if (arr[i] !== arr[i - 1] * a + b && flag) {
      console.log("B");
      flag = false;
    }
  }

  if (flag) {
    console.log(arr[N - 1] * a + b);
  }
}
