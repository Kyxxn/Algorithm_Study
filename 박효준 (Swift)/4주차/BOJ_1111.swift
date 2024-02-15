// 24년 겨울 알고리즘 스터디
// BOJ & 프로그래머스
//
// Created by 박효준 on 1/10/24.
// 구현 & BFS

import Foundation

var puyo: [[Character]] = []
for i in 0..<12 {
    // 필드 정보 초기화
    let input = readLine()!
    let row = Array(input)
    puyo.append(row)
}

func BFS(_ i: Int, _ j: Int) {
    var visited: [[Bool]] = Array(repeating: Array(repeating: false, count: 6+1), count: 12+1)
    var queue: [(Int, Int)] = []
    let mx = [0,0,-1,1]
    let my = [-1,1,0,0]
    visited[i][j] = true
    queue.append((i,j))
    
    while !queue.isEmpty {
        let tmp = queue.removeFirst()
        for next in 0..<4 {
            let curChar = puyo[i][j]
            let nextX = tmp.0 + mx[next]
            let nextY = tmp.1 + my[next]
            if !visited[nextX][nextY] && nextX > 0 && nextX < 13 && nextY > 0 && nextY < 7 {
                if puyo[nextX][nextY] == curChar {
                    
                }
            }
        }
    }
}

for i in 0..<12 {
    for j in 0..<6 {
        BFS(i,j)
    }
}
