const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "ex.txt";
const input = fs.readFileSync(filePath, "utf8").trim().split("\n");

const N = Number(input[0]);

const prime = { 1: true };
const SIZE = 1003001;
const che = Math.sqrt(SIZE);

for (let i = 2; i <= che; i++) {
  if (prime[i]) continue;
  for (let j = i * 2; j <= SIZE; j += i) {
    prime[j] = true;
  }
}

for (let i = N; i <= SIZE; i++) {
  if (prime[i]) continue;
  else {
    if (i.length === 1) {
      console.log(i);
      break;
    }
    const str = i.toString();
    const compare = str.split("").reverse().join("");
    if (str === compare) {
      console.log(str);
      break;
    }
  }
}
