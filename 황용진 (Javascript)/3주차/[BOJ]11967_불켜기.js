class Node {
  constructor(item) {
    this.item = item;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  push(item) {
    const node = new Node(item);
    if (this.head == null) {
      this.head = node;
    } else {
      this.tail.next = node;
    }

    this.tail = node;
    this.length += 1;
  }

  pop() {
    const popItem = this.head;
    this.head = this.head.next;
    this.length -= 1;
    return popItem.item;
  }
}

const fs = require("fs");
const input = fs
  .readFileSync("./dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map(Number));
const [N, M] = input.shift();

const dx = [0, 0, 1, -1];
const dy = [1, -1, 0, 0];
let room = Array.from(Array(N), () => Array(N).fill(0));

const light = new Map();

input.forEach((v) => {
  const [x, y, a, b] = v.map((v) => v - 1);
  const key = `${x}_${y}`;
  if (light.has(key)) {
    light.set(key, [...light.get(key), [a, b]]);
  } else {
    light.set(key, [[a, b]]);
  }
});

room[0][0] = 2;
const q1 = new Queue();
const q2 = new Queue();
q1.push([0, 0]);
let answer = 1;

while (q1.length > 0) {
  const [x, y] = q1.pop();
  const key = `${x}_${y}`;

  const value = light.get(key);
  if (value) {
    // 불켜기
    value.forEach((v) => {
      const [a, b] = v;
      if (room[a][b] == 0) {
        room[a][b] = 1;
        q2.push([a, b]);
        answer++;
      }
    });
  }

  for (let i = 0; i < q2.length; i++) {
    const [x, y] = q2.pop();
    let flag = false;
    for (let k = 0; k < 4; k++) {
      const nx = x + dx[k];
      const ny = y + dy[k];
      if (nx < 0 || nx >= N || ny < 0 || ny >= N || room[nx][ny] == 0) continue;

      if (room[nx][ny] == 2) {
        room[x][y] = 2;
        q1.push([x, y]);
        flag = true;
        break;
      }
    }

    if (!flag) {
      q2.push([x, y]);
    }
  }
}

console.log(answer);
