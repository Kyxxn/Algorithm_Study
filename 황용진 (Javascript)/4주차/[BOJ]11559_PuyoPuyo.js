const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "ex.txt";
const input = fs
  .readFileSync(filePath, "utf8")
  .trim()
  .split("\n")
  .map((ele) => ele.trim().split(""));

/*
  구현 순서
  1. 필드를 탐색하여 같은 색의 블럭이 4개이상 연결되어 있으면 필드에서 제거 - BFS문제
  2. 필드에서 제거된 블럭 위에 있던 블럭들이 아래로 떨어짐 - 구현문제
*/

// 상, 하, 좌, 우 이동 좌표
const dx = [0, 0, 1, -1];
const dy = [1, -1, 0, 0];
// 방문 배열
let visited;

// 블럭 제거 후 위에 블럭들이 떨어지는 함수
function drop(arr) {
  for (let i = 0; i < 6; i++) {
    let [x, y] = [11, i];
    const empty = Array.from({ length: 12 }, () => null);
    let pIndex = 0;
    let cIndex = 0;

    while (x >= 0) {
      if (arr[x][y] === ".") {
        empty[pIndex++] = [x, y];
      } else {
        if (cIndex < pIndex) {
          const [ex, ey] = empty[cIndex++];
          arr[ex][ey] = arr[x][y];
          arr[x][y] = ".";
          empty[pIndex++] = [x, y];
        }
      }
      [x, y] = [x - 1, y];
    }
  }
}

function bfs(x, y, arr) {
  const block = [[x, y]];
  const queue = [[x, y]];
  let index = 0;
  visited[x][y] = true;
  while (index < queue.length) {
    const [cx, cy] = queue[index++];
    for (let i = 0; i < 4; i++) {
      const [nx, ny] = [cx + dx[i], cy + dy[i]];

      if (nx >= 0 && nx < 12 && ny >= 0 && ny < 6) {
        if (visited[nx][ny]) continue;
        if (arr[nx][ny] !== arr[x][y] || arr[nx][ny] === ".") continue;
        queue.push([nx, ny]);
        visited[nx][ny] = true;
        block.push([nx, ny]);
      }
    }
  }
  if (block.length >= 4) {
    for (const [bx, by] of block) {
      arr[bx][by] = ".";
    }
  }
}

function solution(arr) {
  let cur = ".";
  let cnt = 0;

  let x = 0;
  let y = 0;
  while (true) {
    cur = ".";
    visited = Array.from({ length: 12 }, () =>
      Array.from({ length: 6 }, () => false)
    );
    for (let i = 0; i < 12; i++) {
      for (let j = 0; j < 6; j++) {
        if (arr[i][j] !== "." && !visited[i][j]) {
          cur = arr[i][j];
          x = i;
          y = j;
          bfs(x, y, arr);
        }
      }
    }

    if (cur === ".") break;

    drop(arr);
    cnt++;
  }

  return cnt;
}

console.log(solution(input));
