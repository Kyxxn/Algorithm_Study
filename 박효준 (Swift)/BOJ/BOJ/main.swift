// 24년 겨울 알고리즘 스터디
// BOJ & 프로그래머스
//
// Created by 박효준 on 1/10/24.

import Foundation

func solution(_ n: Int, _ m: Int, _ x: Int, _ y: Int, _ r: Int, _ c: Int, _ k: Int) -> String {
    let dx = [1, 0, 0, -1] // Down, Left, Right, Up 순서
    let dy = [0, -1, 1, 0]
    let ds = ["d", "l", "r", "u"]
    var answer: String = ""

    func dfs(_ x: Int, _ y: Int, _ string: String, _ move: Int, _ n: Int, _ m: Int, _ r: Int, _ c: Int, _ k: Int) {
        // 남은 횟수 안에 도착지까지 갈 수 없는 경우 stop
        if k < move + abs(x - r) + abs(y - c) {
            return
        }
        
        // 정답을 찾은 경우
        if move == k && x == r && y == c {
            answer = string
            return
        }
        
        // 사전 순으로 탐색
        for i in 0..<4 {
            let nx = x + dx[i]
            let ny = y + dy[i]
            
            if nx > 0 && nx <= n && ny > 0 && ny <= m && answer.isEmpty {
                dfs(nx, ny, string + ds[i], move + 1, n, m, r, c, k)
            }
        }
    }

    let minMove = abs(r - x) + abs(c - y) // 도착지까지의 최소 이동 횟수
    // 최소 이동 횟수가 k보다 많거나,
    // 최소 이동 횟수 제외한 이동 횟수가 홀 수인 경우에는 도착지에 도착 불가능
    if minMove > k || (k - minMove) % 2 == 1 {
        return "impossible"
    }

    dfs(x, y, "", 0, n, m, r, c, k)
    return answer
}

print(solution(3, 4, 2, 3, 3, 1, 5))
