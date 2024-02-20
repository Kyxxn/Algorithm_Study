const move = [
  [1, 0],
  [0, -1],
  [0, 1],
  [-1, 0],
]; // 하 좌 우 상
const moveDir = ["d", "l", "r", "u"];

let route = "";

function dfs(n, m, x, y, r, c, cnt, curRoute, k) {
  if (route) return;
  if (cnt + Math.abs(x - r) + Math.abs(y - c) > k) return;
  if (cnt === k) {
    if (x === r && y === c) {
      route = curRoute;
    }
    return;
  }

  for (let i = 0; i < 4; i++) {
    const [dx, dy] = [x + move[i][0], y + move[i][1]];

    if (dx > 0 && dx <= n && dy > 0 && dy <= m) {
      dfs(n, m, dx, dy, r, c, cnt + 1, curRoute + moveDir[i], k);
    }
  }
}

function solution(n, m, x, y, r, c, k) {
  var answer = "";

  let fastAnswer = k - (Math.abs(x - r) + Math.abs(y - c));

  if (fastAnswer < 0 || fastAnswer % 2 !== 0) {
    answer = "impossible";
    return answer;
  }

  dfs(n, m, x, y, r, c, 0, "", k);

  if (!route) {
    answer = "impossible";
    return answer;
  }

  answer = route;

  return answer;
}
